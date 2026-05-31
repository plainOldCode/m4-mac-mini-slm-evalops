#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import json
import os
import re
import shutil
import subprocess
import sys
import time
from dataclasses import asdict, dataclass
from pathlib import Path


DEFAULT_PROMPT = """Answer in Korean with exactly one JSON object and no prose.

Task: classify this model smoke test.
Text: 삼성전자는 HBM 공급 확대와 서버 DRAM 수요 회복으로 실적 개선 기대가 커졌다.

Schema:
{"summary": "...", "sentiment": "bullish|neutral|bearish", "companies": ["..."]}
"""


@dataclass(frozen=True)
class Candidate:
    index: int
    category: str
    model_id: str
    url: str
    quant: str
    params: str
    storage_gb: str
    downloads: str
    likes: str
    pipeline_tag: str


@dataclass(frozen=True)
class SweepReport:
    index: int
    model_id: str
    category: str
    url: str
    quant: str
    params: str
    storage_gb: str
    status: str
    download_status: str
    download_elapsed_seconds: float
    eval_elapsed_seconds: float
    returncode: int | None
    elapsed_seconds: float
    output_chars: int
    json_valid: bool
    schema_valid: bool
    think_leak: bool
    output_cleanup_applied: bool
    output_cleanup_reason: str
    recommendation: str
    stderr_tail: str
    output_tail: str
    cleaned_output_tail: str
    cache_dir: str
    cache_bytes_before_cleanup: int
    cleanup_status: str
    cleanup_error: str
    report_path: str


def main() -> int:
    parser = argparse.ArgumentParser(description="Run MLX smoke tests over saved HF candidates.")
    parser.add_argument("--csv", type=Path, default=Path("data/model-candidates/hf-mlx-candidates-top160-2026-05-30.csv"))
    parser.add_argument("--runs-dir", type=Path, default=Path("runs/candidate-sweep-2026-05-30"))
    parser.add_argument("--category", action="append", help="Category to include. Repeatable.")
    parser.add_argument("--start", type=int, default=0, help="Zero-based start in the filtered candidate list.")
    parser.add_argument("--limit", type=int, default=1)
    parser.add_argument("--timeout", type=int, default=240, help="Generation/eval timeout after download completes.")
    parser.add_argument("--download-timeout", type=int, default=1800)
    parser.add_argument("--max-tokens", type=int, default=160)
    parser.add_argument("--prompt-file", type=Path)
    parser.add_argument("--skip-existing", action="store_true")
    args = parser.parse_args()

    prompt = args.prompt_file.read_text() if args.prompt_file else DEFAULT_PROMPT
    candidates = load_candidates(args.csv)
    if args.category:
        allowed = set(args.category)
        candidates = [candidate for candidate in candidates if candidate.category in allowed]
    selected = candidates[args.start : args.start + args.limit]

    args.runs_dir.mkdir(parents=True, exist_ok=True)
    summary_path = args.runs_dir / "summary.jsonl"

    for offset, candidate in enumerate(selected, start=args.start):
        attempt_dir = args.runs_dir / f"{offset + 1:04d}-{safe_name(candidate.model_id)}"
        report_path = attempt_dir / "report.json"
        if args.skip_existing and report_path.exists():
            print(f"SKIP index={offset + 1} model={candidate.model_id} report={report_path}", flush=True)
            continue

        report = run_candidate(
            candidate,
            offset + 1,
            prompt,
            attempt_dir,
            args.download_timeout,
            args.timeout,
            args.max_tokens,
        )
        with summary_path.open("a") as handle:
            handle.write(json.dumps(asdict(report), ensure_ascii=False) + "\n")

        print(
            "RESULT "
            f"index={report.index} "
            f"status={report.status} "
            f"download={report.download_status} "
            f"model={report.model_id} "
            f"download_elapsed={report.download_elapsed_seconds}s "
            f"eval_elapsed={report.eval_elapsed_seconds}s "
            f"cache_deleted={report.cleanup_status} "
            f"report={report.report_path}",
            flush=True,
        )

    return 0


def load_candidates(path: Path) -> list[Candidate]:
    with path.open(newline="") as handle:
        rows = list(csv.DictReader(handle))
    candidates: list[Candidate] = []
    for index, row in enumerate(rows, start=1):
        candidates.append(
            Candidate(
                index=index,
                category=row.get("category", ""),
                model_id=row.get("id", ""),
                url=row.get("url", ""),
                quant=row.get("quant", ""),
                params=row.get("params", ""),
                storage_gb=row.get("storage_gb", ""),
                downloads=row.get("downloads", ""),
                likes=row.get("likes", ""),
                pipeline_tag=row.get("pipeline_tag", ""),
            )
        )
    return candidates


def run_candidate(
    candidate: Candidate,
    sweep_index: int,
    prompt: str,
    attempt_dir: Path,
    download_timeout: int,
    timeout: int,
    max_tokens: int,
) -> SweepReport:
    if attempt_dir.exists():
        shutil.rmtree(attempt_dir)
    attempt_dir.mkdir(parents=True)
    cache_dir = attempt_dir / "model-cache"
    cache_dir.mkdir()

    prompt_path = attempt_dir / "prompt.txt"
    download_stdout_path = attempt_dir / "download_stdout.txt"
    download_stderr_path = attempt_dir / "download_stderr.txt"
    stdout_path = attempt_dir / "model_stdout.txt"
    stderr_path = attempt_dir / "model_stderr.txt"
    cleaned_stdout_path = attempt_dir / "model_stdout.cleaned.txt"
    cleanup_path = attempt_dir / "cleanup.json"
    report_path = attempt_dir / "report.json"
    prompt_path.write_text(prompt)

    env = os.environ.copy()
    env["HF_HOME"] = str(cache_dir / "hf-home")
    env["HF_HUB_CACHE"] = str(cache_dir / "hf-home" / "hub")
    env["TRANSFORMERS_CACHE"] = str(cache_dir / "transformers")

    command = [
        sys.executable,
        "-m",
        "mlx_lm",
        "generate",
        "--model",
        candidate.model_id,
        "--prompt",
        prompt,
        "--max-tokens",
        str(max_tokens),
        "--temp",
        "0.0",
        "--verbose",
        "False",
    ]
    (attempt_dir / "command.json").write_text(json.dumps(command, indent=2, ensure_ascii=False))
    (attempt_dir / "candidate.json").write_text(json.dumps(asdict(candidate), indent=2, ensure_ascii=False))

    total_start = time.perf_counter()
    download_start = time.perf_counter()
    download_status = "error"
    download_stdout = ""
    download_stderr = ""
    download_command = [
        sys.executable,
        "-c",
        (
            "from huggingface_hub import snapshot_download; "
            "import sys; "
            "snapshot_download(repo_id=sys.argv[1], local_files_only=False)"
        ),
        candidate.model_id,
    ]
    (attempt_dir / "download_command.json").write_text(json.dumps(download_command, indent=2, ensure_ascii=False))
    try:
        download = subprocess.run(
            download_command,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=download_timeout,
            env=env,
        )
        download_stdout = download.stdout or ""
        download_stderr = download.stderr or ""
        download_status = "ok" if download.returncode == 0 else "failed"
    except subprocess.TimeoutExpired as exc:
        download_stdout = decode_maybe(exc.stdout)
        download_stderr = decode_maybe(exc.stderr)
        download_status = "timeout"
    except Exception as exc:  # noqa: BLE001
        download_stderr = repr(exc)
        download_status = "error"
    download_elapsed = round(time.perf_counter() - download_start, 3)
    download_stdout_path.write_text(download_stdout)
    download_stderr_path.write_text(download_stderr)

    returncode: int | None = None
    status = "download_failed" if download_status != "ok" else "error"
    stdout = ""
    stderr = ""
    eval_elapsed = 0.0
    if download_status == "ok":
        eval_start = time.perf_counter()
        try:
            completed = subprocess.run(
                command,
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                timeout=timeout,
                env=env,
            )
            returncode = completed.returncode
            stdout = completed.stdout or ""
            stderr = completed.stderr or ""
            status = "ok" if completed.returncode == 0 and stdout.strip() else "failed"
        except subprocess.TimeoutExpired as exc:
            stdout = decode_maybe(exc.stdout)
            stderr = decode_maybe(exc.stderr)
            status = "timeout"
        except Exception as exc:  # noqa: BLE001
            stderr = repr(exc)
            status = "error"
        eval_elapsed = round(time.perf_counter() - eval_start, 3)
    elapsed = round(time.perf_counter() - total_start, 3)

    stdout_path.write_text(stdout)
    stderr_path.write_text(stderr)
    parsed = analyze_output(stdout)
    cleaned_stdout_path.write_text(parsed["cleaned_text"])

    cache_bytes = directory_size(cache_dir)
    cleanup_status = "not_started"
    cleanup_error = ""
    try:
        shutil.rmtree(cache_dir)
        cleanup_status = "deleted"
    except Exception as exc:  # noqa: BLE001
        cleanup_status = "failed"
        cleanup_error = repr(exc)

    cleanup_path.write_text(
        json.dumps(
            {
                "cache_dir": str(cache_dir),
                "cache_bytes_before_cleanup": cache_bytes,
                "cleanup_status": cleanup_status,
                "cleanup_error": cleanup_error,
            },
            indent=2,
            ensure_ascii=False,
        )
    )

    report = SweepReport(
        index=sweep_index,
        model_id=candidate.model_id,
        category=candidate.category,
        url=candidate.url,
        quant=candidate.quant,
        params=candidate.params,
        storage_gb=candidate.storage_gb,
        status=status,
        download_status=download_status,
        download_elapsed_seconds=download_elapsed,
        eval_elapsed_seconds=eval_elapsed,
        returncode=returncode,
        elapsed_seconds=elapsed,
        output_chars=len(stdout),
        json_valid=parsed["json_valid"],
        schema_valid=parsed["schema_valid"],
        think_leak=parsed["think_leak"],
        output_cleanup_applied=parsed["output_cleanup_applied"],
        output_cleanup_reason=parsed["output_cleanup_reason"],
        recommendation=recommend(status, parsed),
        stderr_tail=tail(stderr),
        output_tail=tail(stdout),
        cleaned_output_tail=tail(parsed["cleaned_text"]),
        cache_dir=str(cache_dir),
        cache_bytes_before_cleanup=cache_bytes,
        cleanup_status=cleanup_status,
        cleanup_error=cleanup_error,
        report_path=str(report_path),
    )
    report_path.write_text(json.dumps(asdict(report), indent=2, ensure_ascii=False))
    return report


def directory_size(path: Path) -> int:
    total = 0
    if not path.exists():
        return total
    for child in path.rglob("*"):
        if child.is_file():
            try:
                total += child.stat().st_size
            except OSError:
                pass
    return total


def decode_maybe(value: str | bytes | None) -> str:
    if value is None:
        return ""
    if isinstance(value, bytes):
        return value.decode(errors="replace")
    return value


def analyze_output(text: str) -> dict[str, bool | str]:
    lowered = text.lower()
    think_leak = (
        "<think>" in lowered
        or lowered.startswith(("okay,", "let's", "we need", "i need", "thinking process"))
        or "thinking process:" in lowered[:200]
    )
    cleaned_text, cleanup_reason = clean_reasoning_wrappers(text)
    obj = extract_json_object(cleaned_text)
    schema_valid = False
    if isinstance(obj, dict):
        schema_valid = (
            isinstance(obj.get("summary"), str)
            and obj.get("sentiment") in {"bullish", "neutral", "bearish"}
            and isinstance(obj.get("companies"), list)
            and all(isinstance(item, str) for item in obj.get("companies", []))
        )
    return {
        "json_valid": isinstance(obj, dict),
        "schema_valid": schema_valid,
        "think_leak": think_leak,
        "output_cleanup_applied": cleaned_text != text,
        "output_cleanup_reason": cleanup_reason,
        "cleaned_text": cleaned_text,
    }


def clean_reasoning_wrappers(text: str) -> tuple[str, str]:
    blocks = re.findall(r"<think>(.*?)</think>\s*", text, flags=re.S | re.I)
    if not blocks:
        return text, "none"
    cleaned = re.sub(r"<think>.*?</think>\s*", "", text, flags=re.S | re.I).lstrip()
    if all(not block.strip() for block in blocks):
        return cleaned, "empty_think_wrapper_removed"
    return cleaned, "think_block_removed"


def extract_json_object(text: str) -> object | None:
    fenced = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", text, re.S)
    candidates = [fenced.group(1)] if fenced else []
    brace = re.search(r"(\{.*\})", text, re.S)
    if brace:
        candidates.append(brace.group(1))
    for candidate in candidates:
        try:
            return json.loads(candidate)
        except json.JSONDecodeError:
            continue
    return None


def recommend(status: str, parsed: dict[str, bool | str]) -> str:
    if status == "download_failed":
        return "download_failed"
    if status == "timeout":
        return "generation_timeout_after_download"
    if status != "ok":
        return "task_type_or_runtime_mismatch"
    if parsed["schema_valid"] and parsed["output_cleanup_applied"]:
        return "candidate_for_core_tasks_after_cleanup"
    if parsed["schema_valid"] and not parsed["think_leak"]:
        return "candidate_for_core_tasks"
    if parsed["schema_valid"] and parsed["think_leak"]:
        return "candidate_for_two_pass_cleanup"
    if parsed["json_valid"] and not parsed["schema_valid"]:
        return "partial_schema_candidate"
    if parsed["think_leak"]:
        return "reasoning_lane_protocol_mismatch"
    return "non_core_unstructured_output"


def tail(text: str, max_chars: int = 2000) -> str:
    return text[-max_chars:]


def safe_name(value: str) -> str:
    safe = "".join(char if char.isalnum() else "-" for char in value)
    while "--" in safe:
        safe = safe.replace("--", "-")
    return safe.strip("-")[:96]


if __name__ == "__main__":
    raise SystemExit(main())
