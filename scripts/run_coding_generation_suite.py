#!/usr/bin/env python3
from __future__ import annotations

import argparse
import difflib
import json
import os
import re
import shutil
import subprocess
import sys
import time
import urllib.error
import urllib.request
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

from run_mlx_candidate_sweep import directory_size, safe_name
from run_multilingual_prompt_suite import decode_maybe, tail


@dataclass(frozen=True)
class CodingTask:
    task_id: str
    stage: str
    language: str
    title: str
    description: str
    instructions: list[str]
    task_dir: Path
    test_command: list[str]
    allowed_paths: list[str]


@dataclass(frozen=True)
class CodingTaskResult:
    task_id: str
    stage: str
    language: str
    status: str
    generation_elapsed_seconds: float
    test_elapsed_seconds: float
    returncode: int | None
    json_valid: bool
    schema_valid: bool
    changed: bool
    tests_passed: bool
    diff_lines: int
    applied_paths: list[str]
    rejected_paths: list[str]
    error_tail: str


def main() -> int:
    parser = argparse.ArgumentParser(description="Run deterministic coding-generation tasks.")
    parser.add_argument("--candidates", type=Path, default=Path("data/benchmark/coding-generation-smoke-candidates-2026-06-01.json"))
    parser.add_argument("--prompt-pack", type=Path, default=Path("data/benchmark/coding-generation-prompt-pack-v1.json"))
    parser.add_argument("--runs-dir", type=Path, default=Path("runs/coding-generation-smoke-2026-06-01"))
    parser.add_argument("--report-json", type=Path, default=Path("reports/small-models/coding-generation-smoke-2026-06-01.json"))
    parser.add_argument("--report-md", type=Path, default=Path("reports/small-models/coding-generation-smoke-2026-06-01.md"))
    parser.add_argument("--stage", default="v1_smoke")
    parser.add_argument("--start", type=int, default=0)
    parser.add_argument("--limit", type=int, default=1)
    parser.add_argument("--timeout", type=int, default=180)
    parser.add_argument("--download-timeout", type=int, default=1800)
    parser.add_argument("--max-tokens", type=int, default=1800)
    parser.add_argument("--static-output-dir", type=Path, help="Directory containing one JSON output per task: <task_id>.json")
    parser.add_argument("--skip-existing", action="store_true")
    args = parser.parse_args()

    candidates = load_candidates(args.candidates)
    tasks = load_tasks(args.prompt_pack, args.stage)
    selected = candidates[args.start : args.start + args.limit]

    args.runs_dir.mkdir(parents=True, exist_ok=True)
    args.report_json.parent.mkdir(parents=True, exist_ok=True)
    args.report_md.parent.mkdir(parents=True, exist_ok=True)
    (args.runs_dir / "tasks.expanded.json").write_text(json.dumps([asdict(task) for task in tasks], indent=2, default=str))

    for local_index, candidate in enumerate(selected, start=args.start + 1):
        candidate_dir = args.runs_dir / f"{local_index:04d}-{safe_name(candidate['model_id'])}"
        report_path = candidate_dir / "model_report.json"
        if args.skip_existing and report_path.exists():
            print(f"SKIP model={candidate['model_id']} report={report_path}", flush=True)
            continue

        report = run_candidate(candidate, tasks, candidate_dir, args)
        append_jsonl(args.runs_dir / "summary.jsonl", report)
        write_reports(args.runs_dir, args.report_json, args.report_md)
        print(
            "CODING_RESULT "
            f"model={report['model_id']} "
            f"backend={report['backend']} "
            f"download={report.get('download_status', 'n/a')} "
            f"json={report['json_valid_count']}/{report['task_count']} "
            f"schema={report['schema_valid_count']}/{report['task_count']} "
            f"pass={report['tests_passed_count']}/{report['task_count']} "
            f"cache={report.get('cleanup_status', 'n/a')} "
            f"report={report_path}",
            flush=True,
        )

    return 0


def load_candidates(path: Path) -> list[dict[str, str]]:
    return json.loads(path.read_text())["candidates"]


def load_tasks(prompt_pack: Path, stage_id: str) -> list[CodingTask]:
    data = json.loads(prompt_pack.read_text())
    stage = next((item for item in data["stages"] if item["id"] == stage_id), None)
    if not stage:
        raise ValueError(f"stage not found: {stage_id}")
    tasks: list[CodingTask] = []
    for task_dir_text in stage.get("task_dirs", []):
        task_dir = Path(task_dir_text)
        meta = json.loads((task_dir / "task.json").read_text())
        tasks.append(
            CodingTask(
                task_id=meta["id"],
                stage=meta["stage"],
                language=meta["language"],
                title=meta["title"],
                description=meta["description"],
                instructions=list(meta["instructions"]),
                task_dir=task_dir,
                test_command=list(meta["test_command"]),
                allowed_paths=list(meta["allowed_paths"]),
            )
        )
    return tasks


def run_candidate(candidate: dict[str, str], tasks: list[CodingTask], candidate_dir: Path, args: argparse.Namespace) -> dict[str, Any]:
    if candidate_dir.exists():
        shutil.rmtree(candidate_dir)
    candidate_dir.mkdir(parents=True)
    (candidate_dir / "candidate.json").write_text(json.dumps(candidate, indent=2, ensure_ascii=False))

    backend = candidate.get("backend", "mlx")
    total_start = time.perf_counter()
    cache_dir = candidate_dir / "model-cache"
    env = os.environ.copy()
    download_status = "not_required"
    download_elapsed = 0.0
    cache_bytes = 0
    cleanup_status = "not_required"
    cleanup_error = ""

    if backend == "mlx":
        cache_dir.mkdir()
        env["HF_HOME"] = str(cache_dir / "hf-home")
        env["HF_HUB_CACHE"] = str(cache_dir / "hf-home" / "hub")
        env["TRANSFORMERS_CACHE"] = str(cache_dir / "transformers")
        download_status, download_elapsed, download_stdout, download_stderr = download_model(
            candidate["model_id"], env, args.download_timeout
        )
        (candidate_dir / "download_stdout.txt").write_text(download_stdout)
        (candidate_dir / "download_stderr.txt").write_text(download_stderr)

    results: list[CodingTaskResult] = []
    for task in tasks:
        if backend == "mlx" and download_status != "ok":
            results.append(download_failed_result(task, download_status))
            continue
        results.append(run_task(candidate, task, candidate_dir, env, args))

    if cache_dir.exists():
        cache_bytes = directory_size(cache_dir)
        try:
            shutil.rmtree(cache_dir)
            cleanup_status = "deleted"
        except Exception as exc:  # noqa: BLE001
            cleanup_status = "failed"
            cleanup_error = repr(exc)

    report = {
        "model_id": candidate["model_id"],
        "backend": backend,
        "routing_label": candidate.get("routing_label", ""),
        "task_count": len(results),
        "download_status": download_status,
        "download_elapsed_seconds": download_elapsed,
        "elapsed_seconds": round(time.perf_counter() - total_start, 3),
        "json_valid_count": sum(1 for item in results if item.json_valid),
        "schema_valid_count": sum(1 for item in results if item.schema_valid),
        "changed_count": sum(1 for item in results if item.changed),
        "tests_passed_count": sum(1 for item in results if item.tests_passed),
        "cache_bytes_before_cleanup": cache_bytes,
        "cleanup_status": cleanup_status,
        "cleanup_error": cleanup_error,
        "results": [asdict(item) for item in results],
    }
    (candidate_dir / "model_report.json").write_text(json.dumps(report, indent=2, ensure_ascii=False))
    (candidate_dir / "model_report.md").write_text(render_model_markdown(report))
    return report


def run_task(
    candidate: dict[str, str],
    task: CodingTask,
    candidate_dir: Path,
    env: dict[str, str],
    args: argparse.Namespace,
) -> CodingTaskResult:
    task_dir = candidate_dir / "tasks" / task.task_id
    attempt_repo = task_dir / "repo"
    task_dir.mkdir(parents=True)
    shutil.copytree(task.task_dir / "repo", attempt_repo)
    (task_dir / "prompt.txt").write_text(render_prompt(task))

    before = snapshot_files(attempt_repo)
    generation_start = time.perf_counter()
    raw_output, generation_status, generation_error = generate_output(candidate, task, task_dir, env, args)
    generation_elapsed = round(time.perf_counter() - generation_start, 3)
    (task_dir / "raw_output.txt").write_text(raw_output)

    parsed = extract_json_object(raw_output)
    json_valid = isinstance(parsed, dict)
    schema_valid = False
    applied_paths: list[str] = []
    rejected_paths: list[str] = []
    error_tail = generation_error

    if json_valid:
        schema_valid, applied_paths, rejected_paths, apply_error = apply_model_files(parsed, attempt_repo, task.allowed_paths)
        if apply_error:
            error_tail = apply_error
    else:
        error_tail = generation_error or "No parseable JSON object in model output."

    after_apply = snapshot_files(attempt_repo)
    changed = before != after_apply

    test_start = time.perf_counter()
    returncode: int | None = None
    stdout = ""
    stderr = ""
    tests_passed = False
    if schema_valid:
        try:
            completed = subprocess.run(
                task.test_command,
                cwd=attempt_repo,
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                timeout=args.timeout,
            )
            returncode = completed.returncode
            stdout = completed.stdout
            stderr = completed.stderr
            tests_passed = completed.returncode == 0
        except subprocess.TimeoutExpired as exc:
            returncode = None
            stdout = decode_maybe(exc.stdout)
            stderr = decode_maybe(exc.stderr) + "\nTEST_TIMEOUT"
        except FileNotFoundError as exc:
            stderr = repr(exc)
        except Exception as exc:  # noqa: BLE001
            stderr = repr(exc)
    else:
        stderr = error_tail
    test_elapsed = round(time.perf_counter() - test_start, 3)

    after = snapshot_files(attempt_repo)
    diff_text = build_diff(before, after)
    (task_dir / "diff.patch").write_text(diff_text)
    (task_dir / "stdout.txt").write_text(stdout)
    (task_dir / "stderr.txt").write_text(stderr)

    return CodingTaskResult(
        task_id=task.task_id,
        stage=task.stage,
        language=task.language,
        status=generation_status,
        generation_elapsed_seconds=generation_elapsed,
        test_elapsed_seconds=test_elapsed,
        returncode=returncode,
        json_valid=json_valid,
        schema_valid=schema_valid,
        changed=changed,
        tests_passed=tests_passed,
        diff_lines=len(diff_text.splitlines()),
        applied_paths=applied_paths,
        rejected_paths=rejected_paths,
        error_tail=tail(stderr or error_tail),
    )


def render_prompt(task: CodingTask) -> str:
    instructions = "\n".join(f"- {item}" for item in task.instructions)
    allowed_paths = "\n".join(f"- {item}" for item in task.allowed_paths)
    repo_files = "\n\n".join(
        render_file(path)
        for path in sorted((task.task_dir / "repo").rglob("*"))
        if path.is_file() and should_include_prompt_file(path)
    )
    return f"""You are being evaluated for coding generation.

Task: {task.title}
Language: {task.language}
Description: {task.description}

Instructions:
{instructions}

Allowed output paths:
{allowed_paths}

Return exactly one JSON object and no markdown fences:
{{"files":[{{"path":"relative/path.ext","content":"complete replacement file content"}}]}}

Current repository files:
{repo_files}
"""


def render_file(path: Path) -> str:
    relative = path.relative_to(path.parents[2])
    return f"### {relative}\n```\n{path.read_text(errors='replace')}\n```"


def should_include_prompt_file(path: Path) -> bool:
    if "__pycache__" in path.parts:
        return False
    if path.suffix in {".pyc", ".pyo"}:
        return False
    return True


def generate_output(
    candidate: dict[str, str],
    task: CodingTask,
    task_dir: Path,
    env: dict[str, str],
    args: argparse.Namespace,
) -> tuple[str, str, str]:
    backend = candidate.get("backend", "mlx")
    prompt = (task_dir / "prompt.txt").read_text()
    if backend == "scripted":
        return solution_json(task), "ok", ""
    if backend == "static-json":
        if not args.static_output_dir:
            return "", "error", "--static-output-dir is required for static-json backend"
        output_path = args.static_output_dir / f"{task.task_id}.json"
        if not output_path.exists():
            return "", "error", f"missing static output: {output_path}"
        return output_path.read_text(), "ok", ""
    if backend == "openai":
        return generate_openai(candidate["model_id"], prompt, args.timeout, args.max_tokens)
    if backend == "codex-cli":
        return generate_codex_cli(candidate["model_id"], prompt, task_dir, args.timeout)
    if backend == "mlx":
        return generate_mlx(candidate["model_id"], prompt, env, args.timeout, args.max_tokens)
    return "", "error", f"unknown backend: {backend}"


def solution_json(task: CodingTask) -> str:
    files = []
    for relative in task.allowed_paths:
        solution_path = task.task_dir / "solution" / relative
        if solution_path.exists():
            files.append({"path": relative, "content": solution_path.read_text()})
    return json.dumps({"files": files}, ensure_ascii=False)


def generate_mlx(model_id: str, prompt: str, env: dict[str, str], timeout: int, max_tokens: int) -> tuple[str, str, str]:
    command = [
        sys.executable,
        "-m",
        "mlx_lm",
        "generate",
        "--model",
        model_id,
        "--prompt",
        prompt,
        "--max-tokens",
        str(max_tokens),
        "--temp",
        "0.0",
        "--verbose",
        "False",
    ]
    try:
        completed = subprocess.run(command, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=timeout, env=env)
        status = "ok" if completed.returncode == 0 else "failed"
        return completed.stdout or "", status, tail(completed.stderr or "")
    except subprocess.TimeoutExpired as exc:
        return decode_maybe(exc.stdout), "timeout", tail(decode_maybe(exc.stderr))
    except Exception as exc:  # noqa: BLE001
        return "", "error", repr(exc)


def generate_openai(model_id: str, prompt: str, timeout: int, max_tokens: int) -> tuple[str, str, str]:
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        return "", "skipped", "OPENAI_API_KEY is not set"
    payload = {
        "model": model_id,
        "input": prompt,
        "max_output_tokens": max_tokens,
        "temperature": 0,
    }
    request = urllib.request.Request(
        "https://api.openai.com/v1/responses",
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:  # noqa: S310
            data = json.loads(response.read().decode("utf-8"))
        output_text = data.get("output_text")
        if output_text:
            return output_text, "ok", ""
        texts: list[str] = []
        for item in data.get("output", []):
            for content in item.get("content", []):
                if content.get("type") in {"output_text", "text"} and "text" in content:
                    texts.append(content["text"])
        return "\n".join(texts), "ok", ""
    except urllib.error.HTTPError as exc:
        return "", "failed", tail(exc.read().decode("utf-8", errors="replace"))
    except Exception as exc:  # noqa: BLE001
        return "", "error", repr(exc)


def generate_codex_cli(model_id: str, prompt: str, task_dir: Path, timeout: int) -> tuple[str, str, str]:
    codex_home = os.environ.get("CODEX_CLI_AUTH_HOME") or str(Path.home() / ".codex")
    output_path = task_dir / "codex_last_message.txt"
    sandbox_dir = task_dir / "codex-empty-workdir"
    sandbox_dir.mkdir()
    command = [
        "codex",
        "exec",
        "--ephemeral",
        "--model",
        model_id,
        "--sandbox",
        "read-only",
        "-C",
        str(sandbox_dir),
        "-o",
        str(output_path),
        prompt,
    ]
    env = os.environ.copy()
    env["CODEX_HOME"] = codex_home
    try:
        completed = subprocess.run(command, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=timeout, env=env)
        if output_path.exists():
            output = output_path.read_text()
        else:
            output = completed.stdout or ""
        status = "ok" if completed.returncode == 0 else "failed"
        return output, status, tail(completed.stderr or completed.stdout or "")
    except subprocess.TimeoutExpired as exc:
        return output_path.read_text() if output_path.exists() else decode_maybe(exc.stdout), "timeout", tail(decode_maybe(exc.stderr))
    except Exception as exc:  # noqa: BLE001
        return "", "error", repr(exc)


def download_model(model_id: str, env: dict[str, str], timeout: int) -> tuple[str, float, str, str]:
    start = time.perf_counter()
    command = [
        sys.executable,
        "-c",
        (
            "from huggingface_hub import snapshot_download; "
            "import sys; "
            "snapshot_download(repo_id=sys.argv[1], local_files_only=False)"
        ),
        model_id,
    ]
    try:
        completed = subprocess.run(command, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=timeout, env=env)
        status = "ok" if completed.returncode == 0 else "failed"
        stdout = completed.stdout or ""
        stderr = completed.stderr or ""
    except subprocess.TimeoutExpired as exc:
        status = "timeout"
        stdout = decode_maybe(exc.stdout)
        stderr = decode_maybe(exc.stderr)
    except Exception as exc:  # noqa: BLE001
        status = "error"
        stdout = ""
        stderr = repr(exc)
    return status, round(time.perf_counter() - start, 3), stdout, stderr


def extract_json_object(text: str) -> dict[str, Any] | None:
    stripped = text.strip()
    if stripped.startswith("```"):
        stripped = re.sub(r"^```(?:json)?\s*", "", stripped)
        stripped = re.sub(r"\s*```$", "", stripped)
    try:
        parsed = json.loads(stripped)
        return parsed if isinstance(parsed, dict) else None
    except json.JSONDecodeError:
        pass
    match = re.search(r"\{.*\}", stripped, re.DOTALL)
    if not match:
        return None
    try:
        parsed = json.loads(match.group(0))
    except json.JSONDecodeError:
        return None
    return parsed if isinstance(parsed, dict) else None


def apply_model_files(parsed: dict[str, Any], attempt_repo: Path, allowed_paths: list[str]) -> tuple[bool, list[str], list[str], str]:
    files = parsed.get("files")
    if not isinstance(files, list):
        return False, [], [], "JSON object must contain files array."
    allowed = set(allowed_paths)
    applied: list[str] = []
    rejected: list[str] = []
    for item in files:
        if not isinstance(item, dict) or not isinstance(item.get("path"), str) or not isinstance(item.get("content"), str):
            return False, applied, rejected, "Each file entry must contain string path and content."
        relative = item["path"]
        if relative.startswith("/") or ".." in Path(relative).parts or relative not in allowed:
            rejected.append(relative)
            continue
        target = attempt_repo / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(item["content"])
        applied.append(relative)
    return bool(applied) and not rejected, applied, rejected, ""


def snapshot_files(root: Path) -> dict[str, str]:
    files: dict[str, str] = {}
    for path in sorted(root.rglob("*")):
        if path.is_file() and "__pycache__" not in path.parts and path.suffix not in {".pyc", ".pyo"}:
            files[str(path.relative_to(root))] = path.read_text(errors="replace")
    return files


def build_diff(before: dict[str, str], after: dict[str, str]) -> str:
    chunks: list[str] = []
    for name in sorted(set(before) | set(after)):
        old = before.get(name, "").splitlines(keepends=True)
        new = after.get(name, "").splitlines(keepends=True)
        if old == new:
            continue
        chunks.extend(difflib.unified_diff(old, new, fromfile=f"a/{name}", tofile=f"b/{name}"))
    return "".join(chunks)


def download_failed_result(task: CodingTask, status: str) -> CodingTaskResult:
    return CodingTaskResult(
        task_id=task.task_id,
        stage=task.stage,
        language=task.language,
        status=f"download_{status}",
        generation_elapsed_seconds=0.0,
        test_elapsed_seconds=0.0,
        returncode=None,
        json_valid=False,
        schema_valid=False,
        changed=False,
        tests_passed=False,
        diff_lines=0,
        applied_paths=[],
        rejected_paths=[],
        error_tail=f"download_status={status}",
    )


def append_jsonl(path: Path, item: dict[str, Any]) -> None:
    with path.open("a") as handle:
        handle.write(json.dumps(item, ensure_ascii=False) + "\n")


def write_reports(runs_dir: Path, report_json: Path, report_md: Path) -> None:
    reports = []
    for line in (runs_dir / "summary.jsonl").read_text().splitlines():
        if line.strip():
            reports.append(json.loads(line))
    report_json.write_text(json.dumps({"models": reports}, indent=2, ensure_ascii=False))
    report_md.write_text(render_suite_markdown(reports))


def render_suite_markdown(reports: list[dict[str, Any]]) -> str:
    lines = [
        "# Coding Generation Smoke Suite",
        "",
        "| Rank | Model | Backend | Pass | JSON | Schema | Changed | Elapsed |",
        "| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: |",
    ]
    ranked = sorted(
        reports,
        key=lambda item: (
            item["tests_passed_count"],
            item["schema_valid_count"],
            item["json_valid_count"],
            -item["elapsed_seconds"],
        ),
        reverse=True,
    )
    for rank, report in enumerate(ranked, start=1):
        lines.append(
            "| "
            f"{rank} | `{report['model_id']}` | {report['backend']} | "
            f"{report['tests_passed_count']}/{report['task_count']} | "
            f"{report['json_valid_count']}/{report['task_count']} | "
            f"{report['schema_valid_count']}/{report['task_count']} | "
            f"{report['changed_count']}/{report['task_count']} | "
            f"{report['elapsed_seconds']}s |"
        )
    lines.extend(["", "## Per Model", ""])
    for report in ranked:
        lines.append(render_model_markdown(report))
        lines.append("")
    return "\n".join(lines)


def render_model_markdown(report: dict[str, Any]) -> str:
    lines = [
        f"### {report['model_id']}",
        "",
        f"- Backend: `{report['backend']}`",
        f"- Pass: {report['tests_passed_count']}/{report['task_count']}",
        f"- JSON valid: {report['json_valid_count']}/{report['task_count']}",
        f"- Schema valid: {report['schema_valid_count']}/{report['task_count']}",
        f"- Changed: {report['changed_count']}/{report['task_count']}",
        f"- Download: {report.get('download_status', 'n/a')} in {report.get('download_elapsed_seconds', 0)}s",
        f"- Cache cleanup: {report.get('cleanup_status', 'n/a')}",
        "",
        "| Task | Language | Status | JSON | Schema | Changed | Pass | Diff |",
        "| --- | --- | --- | --- | --- | --- | --- | ---: |",
    ]
    for result in report["results"]:
        lines.append(
            "| "
            f"{result['task_id']} | {result['language']} | {result['status']} | "
            f"{yes_no(result['json_valid'])} | {yes_no(result['schema_valid'])} | "
            f"{yes_no(result['changed'])} | {yes_no(result['tests_passed'])} | "
            f"{result['diff_lines']} |"
        )
    return "\n".join(lines)


def yes_no(value: bool) -> str:
    return "yes" if value else "no"


if __name__ == "__main__":
    raise SystemExit(main())
