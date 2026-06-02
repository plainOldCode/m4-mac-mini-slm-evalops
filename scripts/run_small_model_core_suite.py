#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import time
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from local_model_backends import backend_of, generate_ollama, pull_ollama_model
from run_mlx_candidate_sweep import clean_reasoning_wrappers, directory_size, extract_json_object, safe_name
from run_multilingual_prompt_suite import decode_maybe, tail
from run_tool_calling_suite import download_model


@dataclass(frozen=True)
class CoreCase:
    index: int
    lane: str
    case_id: str
    title: str
    prompt: str
    expected: dict[str, Any]
    fixture_dir: str
    solution_dir: str
    allowed_paths: list[str]


@dataclass(frozen=True)
class CoreCaseResult:
    case_id: str
    lane: str
    status: str
    returncode: int | None
    elapsed_seconds: float
    output_chars: int
    json_valid: bool
    schema_valid: bool
    content_match: bool
    case_pass: bool
    cleanup_applied: bool
    cleanup_reason: str
    error_tail: str


def main() -> int:
    parser = argparse.ArgumentParser(description="Run the small-model-core benchmark pack over local candidates.")
    parser.add_argument("--candidates", type=Path, default=Path("data/benchmark/hf-mlx-expanded-next-queue-2026-06-02.json"))
    parser.add_argument("--pack", type=Path, default=Path("benchmark_packs/small-model-core/pack.json"))
    parser.add_argument("--runs-dir", type=Path, default=Path("runs/small-model-core-expanded-2026-06-02"))
    parser.add_argument("--report-json", type=Path, default=Path("reports/small-models/small-model-core-expanded-2026-06-02.json"))
    parser.add_argument("--report-md", type=Path, default=Path("reports/small-models/small-model-core-expanded-2026-06-02.md"))
    parser.add_argument("--candidate-lane", action="append", help="Candidate lane to include, e.g. text_core. Repeatable.")
    parser.add_argument("--case-lane", action="append", help="Pack lane to include, e.g. summary. Repeatable.")
    parser.add_argument("--start", type=int, default=0, help="Zero-based candidate offset after lane filtering.")
    parser.add_argument("--limit", type=int, default=1)
    parser.add_argument("--timeout", type=int, default=120)
    parser.add_argument("--download-timeout", type=int, default=1800)
    parser.add_argument("--max-tokens", type=int, default=360)
    parser.add_argument("--skip-existing", action="store_true")
    args = parser.parse_args()

    candidates = load_candidates(args.candidates)
    if args.candidate_lane:
        allowed_candidate_lanes = set(args.candidate_lane)
        candidates = [candidate for candidate in candidates if candidate.get("lane") in allowed_candidate_lanes]
    selected = candidates[args.start : args.start + args.limit]

    cases = build_cases(args.pack)
    if args.case_lane:
        allowed_case_lanes = set(args.case_lane)
        cases = [case for case in cases if case.lane in allowed_case_lanes]

    args.runs_dir.mkdir(parents=True, exist_ok=True)
    (args.runs_dir / "pack.expanded.json").write_text(json.dumps([asdict(case) for case in cases], indent=2, ensure_ascii=False))

    for local_index, candidate in enumerate(selected, start=args.start + 1):
        attempt_dir = args.runs_dir / f"{local_index:04d}-{safe_name(candidate['model_id'])}"
        model_report = attempt_dir / "model_report.json"
        if args.skip_existing and model_report.exists():
            print(f"SKIP model={candidate['model_id']} report={model_report}", flush=True)
            continue

        report = run_model(candidate, cases, args.pack.parent, attempt_dir, args.download_timeout, args.timeout, args.max_tokens)
        append_jsonl(args.runs_dir / "summary.jsonl", report)
        write_reports(args.runs_dir, args.report_json, args.report_md)
        print(
            "CORE_RESULT "
            f"model={report['model_id']} "
            f"lane={report.get('lane', '')} "
            f"download={report['download_status']} "
            f"pass={report['case_pass_count']}/{report['case_count']} "
            f"schema={report['schema_valid_count']}/{report['case_count']} "
            f"content={report['content_match_count']}/{report['case_count']} "
            f"cache={report['cleanup_status']} "
            f"report={model_report}",
            flush=True,
        )

    return 0


def load_candidates(path: Path) -> list[dict[str, Any]]:
    return json.loads(path.read_text())["candidates"]


def build_cases(pack_path: Path) -> list[CoreCase]:
    data = json.loads(pack_path.read_text())
    cases: list[CoreCase] = []
    for lane in data["lanes"]:
        for item in lane["cases"]:
            cases.append(
                CoreCase(
                    index=len(cases) + 1,
                    lane=lane["id"],
                    case_id=item["case_id"],
                    title=item["title"],
                    prompt=item["prompt"],
                    expected=item.get("expected", {}),
                    fixture_dir=item.get("fixture_dir", ""),
                    solution_dir=item.get("solution_dir", ""),
                    allowed_paths=list(item.get("allowed_paths", [])),
                )
            )
    return cases


def run_model(
    candidate: dict[str, Any],
    cases: list[CoreCase],
    pack_dir: Path,
    attempt_dir: Path,
    download_timeout: int,
    timeout: int,
    max_tokens: int,
) -> dict[str, Any]:
    if attempt_dir.exists():
        shutil.rmtree(attempt_dir)
    attempt_dir.mkdir(parents=True)
    (attempt_dir / "candidate.json").write_text(json.dumps(candidate, indent=2, ensure_ascii=False))

    backend = backend_of(candidate)
    cache_dir = attempt_dir / "model-cache"
    env = os.environ.copy()
    if backend == "mlx":
        cache_dir.mkdir()
        env["HF_HOME"] = str(cache_dir / "hf-home")
        env["HF_HUB_CACHE"] = str(cache_dir / "hf-home" / "hub")
        env["TRANSFORMERS_CACHE"] = str(cache_dir / "transformers")

    total_start = time.perf_counter()
    if backend == "ollama":
        download_status, download_elapsed, download_stdout, download_stderr = pull_ollama_model(candidate["model_id"], download_timeout)
    else:
        download_status, download_elapsed, download_stdout, download_stderr = download_model(candidate["model_id"], env, download_timeout)
    (attempt_dir / "download_stdout.txt").write_text(download_stdout)
    (attempt_dir / "download_stderr.txt").write_text(download_stderr)

    results: list[CoreCaseResult] = []
    if download_status == "ok":
        for case in cases:
            results.append(run_prompt_case(candidate, case, pack_dir, attempt_dir, env, timeout, max_tokens))
    else:
        for case in cases:
            results.append(
                CoreCaseResult(
                    case_id=case.case_id,
                    lane=case.lane,
                    status="download_not_available",
                    returncode=None,
                    elapsed_seconds=0.0,
                    output_chars=0,
                    json_valid=False,
                    schema_valid=False,
                    content_match=False,
                    case_pass=False,
                    cleanup_applied=False,
                    cleanup_reason="none",
                    error_tail=tail(download_stderr),
                )
            )

    cache_bytes = directory_size(cache_dir) if cache_dir.exists() else 0
    cleanup_status = "not_required" if backend == "ollama" else "not_started"
    cleanup_error = ""
    if cache_dir.exists():
        try:
            shutil.rmtree(cache_dir)
            cleanup_status = "deleted"
        except Exception as exc:  # noqa: BLE001
            cleanup_status = "failed"
            cleanup_error = repr(exc)

    elapsed = round(time.perf_counter() - total_start, 3)
    report = {
        "model_id": candidate["model_id"],
        "backend": backend,
        "lane": candidate.get("lane", ""),
        "params": candidate.get("params", ""),
        "storage_gb": candidate.get("storage_gb", ""),
        "case_count": len(results),
        "download_status": download_status,
        "download_elapsed_seconds": download_elapsed,
        "elapsed_seconds": elapsed,
        "json_valid_count": sum(1 for item in results if item.json_valid),
        "schema_valid_count": sum(1 for item in results if item.schema_valid),
        "content_match_count": sum(1 for item in results if item.content_match),
        "case_pass_count": sum(1 for item in results if item.case_pass),
        "cleanup_count": sum(1 for item in results if item.cleanup_applied),
        "cache_dir": str(cache_dir),
        "cache_bytes_before_cleanup": cache_bytes,
        "cleanup_status": cleanup_status,
        "cleanup_error": cleanup_error,
        "results": [asdict(item) for item in results],
    }
    (attempt_dir / "model_report.json").write_text(json.dumps(report, indent=2, ensure_ascii=False))
    (attempt_dir / "model_report.md").write_text(render_model_markdown(report))
    return report


def run_prompt_case(
    candidate: dict[str, Any],
    case: CoreCase,
    pack_dir: Path,
    attempt_dir: Path,
    env: dict[str, str],
    timeout: int,
    max_tokens: int,
) -> CoreCaseResult:
    model_id = candidate["model_id"]
    backend = backend_of(candidate)
    case_dir = attempt_dir / "raw" / case.case_id
    case_dir.mkdir(parents=True)
    (case_dir / "prompt.json").write_text(json.dumps(asdict(case), indent=2, ensure_ascii=False))
    (case_dir / "prompt.txt").write_text(case.prompt)
    if case.fixture_dir:
        fixture_src = pack_dir / case.fixture_dir
        if fixture_src.exists():
            shutil.copytree(fixture_src, case_dir / "fixture")

    command = ollama_command(model_id, case.prompt, max_tokens) if backend == "ollama" else [
        sys.executable,
        "-m",
        "mlx_lm",
        "generate",
        "--model",
        model_id,
        "--prompt",
        case.prompt,
        "--max-tokens",
        str(max_tokens),
        "--temp",
        "0.0",
        "--verbose",
        "False",
    ]
    (case_dir / "command.json").write_text(json.dumps(command, indent=2, ensure_ascii=False))
    start = time.perf_counter()
    stdout = ""
    stderr = ""
    returncode: int | None = None
    status = "error"
    try:
        if backend == "ollama":
            stdout, status, stderr = generate_ollama(model_id, case.prompt, timeout, max_tokens)
            returncode = 0 if status == "ok" else 1
        else:
            completed = subprocess.run(command, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=timeout, env=env)
            stdout = completed.stdout or ""
            stderr = completed.stderr or ""
            returncode = completed.returncode
            status = "ok" if completed.returncode == 0 and stdout.strip() else "failed"
    except subprocess.TimeoutExpired as exc:
        status = "timeout"
        stdout = decode_maybe(exc.stdout)
        stderr = decode_maybe(exc.stderr)
    except Exception as exc:  # noqa: BLE001
        stderr = repr(exc)
    elapsed = round(time.perf_counter() - start, 3)

    cleaned, cleanup_reason = clean_reasoning_wrappers(stdout)
    parsed = extract_json_object(cleaned)
    metrics = score_case(parsed, case)

    (case_dir / "stdout.txt").write_text(stdout)
    (case_dir / "stdout.cleaned.txt").write_text(cleaned)
    (case_dir / "stderr.txt").write_text(stderr)
    (case_dir / "parsed.json").write_text(json.dumps(parsed, indent=2, ensure_ascii=False))
    result = CoreCaseResult(
        case_id=case.case_id,
        lane=case.lane,
        status=status,
        returncode=returncode,
        elapsed_seconds=elapsed,
        output_chars=len(stdout),
        json_valid=isinstance(parsed, dict),
        schema_valid=metrics["schema_valid"],
        content_match=metrics["content_match"],
        case_pass=metrics["case_pass"],
        cleanup_applied=cleaned != stdout,
        cleanup_reason=cleanup_reason,
        error_tail=tail(stderr),
    )
    (case_dir / "result.json").write_text(json.dumps(asdict(result), indent=2, ensure_ascii=False))
    return result


def score_case(parsed: Any, case: CoreCase) -> dict[str, bool]:
    if not isinstance(parsed, dict):
        return {"schema_valid": False, "content_match": False, "case_pass": False}
    if case.lane == "protocol":
        schema_valid = isinstance(parsed.get("tool_calls"), list) and (
            "final" not in parsed or isinstance(parsed.get("final"), str)
        )
        content_match = score_protocol_case(parsed, case.expected)
    elif case.lane == "patch":
        schema_valid = (
            parsed.get("case_id") == case.case_id
            and isinstance(parsed.get("files"), list)
            and all(isinstance(item, dict) and isinstance(item.get("path"), str) and isinstance(item.get("content"), str) for item in parsed.get("files", []))
            and all(item.get("path") in case.allowed_paths for item in parsed.get("files", []))
        )
        content_match = score_patch_case(parsed, case.expected)
    else:
        schema_valid = parsed.get("case_id") == case.case_id and isinstance(parsed.get("answer"), dict)
        content_match = score_answer_dict(parsed.get("answer") if isinstance(parsed.get("answer"), dict) else {}, case.expected)
    return {
        "schema_valid": schema_valid,
        "content_match": content_match,
        "case_pass": schema_valid and content_match,
    }


def score_answer_dict(answer: dict[str, Any], expected: dict[str, Any]) -> bool:
    for key, expected_value in expected.items():
        if key.endswith("_contains"):
            field = key[: -len("_contains")]
            if not contains_all(answer.get(field), expected_value):
                return False
        elif isinstance(expected_value, list):
            if not list_contains_all(answer.get(key), expected_value):
                return False
        else:
            if normalize_scalar(answer.get(key)) != normalize_scalar(expected_value):
                return False
    return True


def score_protocol_case(parsed: dict[str, Any], expected: dict[str, Any]) -> bool:
    tool_calls = parsed.get("tool_calls")
    if not isinstance(tool_calls, list):
        return False
    if "tool_calls" in expected and tool_calls != expected["tool_calls"]:
        return False
    if "tool_sequence" in expected:
        actual_sequence = [str(call.get("tool_name", "")) for call in tool_calls if isinstance(call, dict)]
        if actual_sequence != expected["tool_sequence"]:
            return False
    if "search_query_contains" in expected:
        if not any(contains_all(call.get("arguments", {}).get("query") if isinstance(call, dict) else "", expected["search_query_contains"]) for call in tool_calls):
            return False
    if "calculator_expression_contains" in expected:
        if not any(contains_all(call.get("arguments", {}).get("expression") if isinstance(call, dict) else "", expected["calculator_expression_contains"]) for call in tool_calls):
            return False
    if "final_contains" in expected and not contains_all(parsed.get("final"), expected["final_contains"]):
        return False
    return True


def score_patch_case(parsed: dict[str, Any], expected: dict[str, Any]) -> bool:
    files = parsed.get("files")
    if not isinstance(files, list):
        return False
    joined = "\n".join(str(item.get("content", "")) for item in files if isinstance(item, dict))
    return contains_all(joined, expected.get("contains", [])) and contains_none(joined, expected.get("does_not_contain", []))


def contains_all(value: Any, needles: Any) -> bool:
    text = normalize_text(value)
    if isinstance(needles, str):
        needles = [needles]
    return all(normalize_text(needle) in text for needle in needles)


def contains_none(value: Any, needles: Any) -> bool:
    text = normalize_text(value)
    if isinstance(needles, str):
        needles = [needles]
    return all(normalize_text(needle) not in text for needle in needles)


def list_contains_all(value: Any, expected_items: list[Any]) -> bool:
    if not isinstance(value, list):
        return False
    normalized_values = [normalize_text(item) for item in value]
    return all(any(normalize_text(expected) in actual or actual in normalize_text(expected) for actual in normalized_values) for expected in expected_items)


def normalize_scalar(value: Any) -> str:
    if isinstance(value, (int, float)):
        return str(value)
    return normalize_text(value)


def normalize_text(value: Any) -> str:
    if isinstance(value, list):
        value = " ".join(str(item) for item in value)
    return " ".join(str(value).lower().strip().split())


def ollama_command(model_id: str, prompt: str, max_tokens: int) -> list[str]:
    return ["ollama", "api", "generate", model_id, f"prompt_chars={len(prompt)}", f"num_predict={max_tokens}"]


def render_model_markdown(report: dict[str, Any]) -> str:
    rows = report["results"]
    lane_counts: dict[str, tuple[int, int]] = {}
    for row in rows:
        lane = str(row["lane"])
        lane_counts[lane] = increment_pair(lane_counts.get(lane, (0, 0)), bool(row["case_pass"]))

    lines = [
        f"# Small Model Core - {report['model_id']}",
        "",
        f"- Cases: {report['case_count']}",
        f"- Download: {report['download_status']} in {report['download_elapsed_seconds']}s",
        f"- JSON valid: {report['json_valid_count']}/{report['case_count']}",
        f"- Schema valid: {report['schema_valid_count']}/{report['case_count']}",
        f"- Content match: {report['content_match_count']}/{report['case_count']}",
        f"- Case pass: {report['case_pass_count']}/{report['case_count']}",
        f"- Cleanup applied: {report['cleanup_count']}",
        f"- Cache cleanup: {report['cleanup_status']}",
        "",
        "## Lane Pass",
        "",
    ]
    for key in sorted(lane_counts):
        matched, total = lane_counts[key]
        lines.append(f"- `{key}`: {matched}/{total}")
    lines.append("")
    return "\n".join(lines)


def write_reports(runs_dir: Path, report_json: Path, report_md: Path) -> None:
    reports = load_reports(runs_dir)
    output = {
        "runs_dir": str(runs_dir),
        "scoring_policy": {
            "case_pass": "Schema-valid JSON plus deterministic content match for the case lane.",
            "lanes": "summary, extraction, protocol, and patch are scored separately before model-level aggregation.",
            "execution_policy": "Patch outputs are not applied to the repo; generated replacement-file content is scored against allowlisted paths and expected text constraints.",
        },
        "models": sorted(reports, key=lambda item: (item["case_pass_count"], item["content_match_count"], item["schema_valid_count"]), reverse=True),
    }
    report_json.parent.mkdir(parents=True, exist_ok=True)
    report_md.parent.mkdir(parents=True, exist_ok=True)
    report_json.write_text(json.dumps(output, indent=2, ensure_ascii=False))
    report_md.write_text(render_suite_markdown(output))


def load_reports(runs_dir: Path) -> list[dict[str, Any]]:
    summary = runs_dir / "summary.jsonl"
    reports: list[dict[str, Any]] = []
    if summary.exists():
        for line in summary.read_text().splitlines():
            if line.strip():
                reports.append(json.loads(line))
    deduped: dict[str, dict[str, Any]] = {}
    for report in reports:
        deduped[str(report["model_id"])] = report
    return list(deduped.values())


def render_suite_markdown(output: dict[str, Any]) -> str:
    lines = [
        "# Small Model Core Suite",
        "",
        "This suite evaluates public-safe summary, extraction, protocol, and patch tasks.",
        "",
        "| Rank | Model | Lane | Pass | Content | Schema | JSON | Cleanup |",
        "| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: |",
    ]
    for rank, model in enumerate(output["models"], start=1):
        total = model["case_count"]
        lines.append(
            f"| {rank} | `{model['model_id']}` | `{model.get('lane', '')}` | "
            f"{model['case_pass_count']}/{total} | "
            f"{model['content_match_count']}/{total} | "
            f"{model['schema_valid_count']}/{total} | "
            f"{model['json_valid_count']}/{total} | "
            f"{model['cleanup_count']} |"
        )
    lines += ["", "## Notes", ""]
    lines.append("- `Pass` requires schema-valid JSON and deterministic content match.")
    lines.append("- Reasoning cleanup is tracked through wrapper cleanup counts and per-case raw artifacts.")
    lines.append("")
    return "\n".join(lines)


def increment_pair(pair: tuple[int, int], matched: bool) -> tuple[int, int]:
    current, total = pair
    return current + int(matched), total + 1


def append_jsonl(path: Path, item: dict[str, Any]) -> None:
    with path.open("a") as handle:
        handle.write(json.dumps(item, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    raise SystemExit(main())
