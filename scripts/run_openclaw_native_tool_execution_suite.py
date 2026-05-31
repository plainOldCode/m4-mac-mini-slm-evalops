#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import tempfile
import time
import uuid
from dataclasses import asdict, dataclass
from pathlib import Path
from urllib.error import URLError
from urllib.request import Request, urlopen

from run_mlx_candidate_sweep import directory_size, safe_name
from run_multilingual_prompt_suite import tail


ROOT = Path(__file__).resolve().parents[1]
WORKSPACE = Path("/Users/miniadmin/.openclaw/workspace")
OPENCLAW_CONFIG = Path("/Users/miniadmin/.openclaw/openclaw.json")
MLX_SERVER = WORKSPACE / ".venv-mlx" / "bin" / "mlx_lm.server"


@dataclass(frozen=True)
class NativeToolResult:
    model_id: str
    rank: int
    provider_id: str
    port: int
    status: str
    marker_created: bool
    marker_content_ok: bool
    output_mentions_marker: bool
    duration_seconds: float
    server_start_seconds: float
    openclaw_returncode: int | None
    prompt_tokens: int | None
    output_tokens: int | None
    cache_read_tokens: int | None
    compaction_count: int | None
    response_text: str
    error_tail: str
    server_log: str
    cache_bytes_before_cleanup: int
    cleanup_status: str


def main() -> int:
    parser = argparse.ArgumentParser(description="Run OpenClaw native tool execution canaries for MLX models.")
    parser.add_argument("--candidates", type=Path, default=ROOT / "data/benchmark/tool-calling-leaders-100prompt-candidates-2026-05-31.json")
    parser.add_argument("--runs-dir", type=Path, default=ROOT / "runs/openclaw-native-tool-execution-2026-05-31")
    parser.add_argument("--report-json", type=Path, default=ROOT / "reports/small-models/openclaw-native-tool-execution-2026-05-31.json")
    parser.add_argument("--report-md", type=Path, default=ROOT / "reports/small-models/openclaw-native-tool-execution-2026-05-31.md")
    parser.add_argument("--start", type=int, default=0)
    parser.add_argument("--limit", type=int, default=10)
    parser.add_argument("--base-port", type=int, default=18100)
    parser.add_argument("--ready-timeout", type=int, default=900)
    parser.add_argument("--agent-timeout", type=int, default=360)
    parser.add_argument("--max-tokens", type=int, default=160)
    parser.add_argument("--keep-cache", action="store_true")
    args = parser.parse_args()

    if not MLX_SERVER.exists():
        raise SystemExit(f"mlx_lm.server not found: {MLX_SERVER}")

    candidates = json.loads(args.candidates.read_text())["candidates"]
    selected = candidates[args.start : args.start + args.limit]
    args.runs_dir.mkdir(parents=True, exist_ok=True)
    args.report_json.parent.mkdir(parents=True, exist_ok=True)

    existing = load_existing(args.runs_dir / "summary.jsonl")
    completed = {item["model_id"] for item in existing if item.get("status") in {"pass", "fail", "error"}}

    for offset, candidate in enumerate(selected, start=args.start):
        model_id = candidate["model_id"]
        if model_id in completed:
            print(f"SKIP existing model={model_id}", flush=True)
            continue
        rank = int(candidate.get("tool_calling_rank", offset + 1))
        port = args.base_port + offset
        attempt_dir = args.runs_dir / f"{rank:02d}-{safe_name(model_id)}"
        result = run_candidate(
            model_id=model_id,
            rank=rank,
            port=port,
            attempt_dir=attempt_dir,
            ready_timeout=args.ready_timeout,
            agent_timeout=args.agent_timeout,
            max_tokens=args.max_tokens,
            keep_cache=args.keep_cache,
        )
        append_jsonl(args.runs_dir / "summary.jsonl", asdict(result))
        write_reports(args.runs_dir / "summary.jsonl", args.report_json, args.report_md)
        print(
            "NATIVE_TOOL_RESULT "
            f"rank={rank} model={model_id} status={result.status} "
            f"marker={result.marker_created}/{result.marker_content_ok} "
            f"duration={result.duration_seconds}s cache={result.cleanup_status}",
            flush=True,
        )

    write_reports(args.runs_dir / "summary.jsonl", args.report_json, args.report_md)
    return 0


def load_existing(path: Path) -> list[dict[str, object]]:
    if not path.exists():
        return []
    rows = []
    for line in path.read_text().splitlines():
        if line.strip():
            rows.append(json.loads(line))
    return rows


def append_jsonl(path: Path, row: dict[str, object]) -> None:
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(row, ensure_ascii=False) + "\n")


def run_candidate(
    *,
    model_id: str,
    rank: int,
    port: int,
    attempt_dir: Path,
    ready_timeout: int,
    agent_timeout: int,
    max_tokens: int,
    keep_cache: bool,
) -> NativeToolResult:
    if attempt_dir.exists():
        shutil.rmtree(attempt_dir)
    attempt_dir.mkdir(parents=True)

    provider_id = f"mlx-native-{rank:02d}"
    cache_dir = attempt_dir / "model-cache"
    cache_dir.mkdir(parents=True)
    (cache_dir / "hf-home" / "hub").mkdir(parents=True, exist_ok=True)
    server_log_path = attempt_dir / "mlx-server.log"
    marker_token = f"native_tool_ok_{uuid.uuid4().hex[:12]}"
    marker_path = Path(tempfile.gettempdir()) / f"openclaw-native-tool-{marker_token}.txt"
    if marker_path.exists():
        marker_path.unlink()

    server_env = os.environ.copy()
    server_env["HF_HOME"] = str(cache_dir / "hf-home")
    server_env["HF_HUB_CACHE"] = str(cache_dir / "hf-home" / "hub")
    server_env["TRANSFORMERS_CACHE"] = str(cache_dir / "transformers")

    command = [
        str(MLX_SERVER),
        "--model",
        model_id,
        "--host",
        "127.0.0.1",
        "--port",
        str(port),
        "--max-tokens",
        str(max_tokens),
        "--log-level",
        "INFO",
    ]

    start = time.perf_counter()
    server_start = start
    server_proc: subprocess.Popen[bytes] | None = None
    log_handle = server_log_path.open("wb")
    try:
        server_proc = subprocess.Popen(
            command,
            cwd=str(WORKSPACE),
            env=server_env,
            stdout=log_handle,
            stderr=subprocess.STDOUT,
        )
        wait_ready(port, server_proc, ready_timeout)
        warm_model(port, model_id, ready_timeout)
        server_start_seconds = round(time.perf_counter() - server_start, 3)

        config_path = write_temp_openclaw_config(provider_id, model_id, port, max_tokens)
        prompt = (
            "Use the exec tool to run exactly this shell command, then reply with one short sentence: "
            f"/bin/sh -lc 'printf {marker_token} > {marker_path}'"
        )
        agent_env = os.environ.copy()
        agent_env["OPENCLAW_CONFIG_PATH"] = str(config_path)
        agent_cmd = [
            "openclaw",
            "agent",
            "--local",
            "--json",
            "--agent",
            "main",
            "--model",
            f"{provider_id}/{model_id}",
            "--session-key",
            f"agent:main:native-tool-{rank:02d}-{uuid.uuid4().hex[:8]}",
            "--timeout",
            str(agent_timeout),
            "--message",
            prompt,
        ]
        completed = subprocess.run(
            agent_cmd,
            cwd=str(WORKSPACE),
            env=agent_env,
            text=True,
            capture_output=True,
            timeout=agent_timeout + 60,
        )
        (attempt_dir / "openclaw_stdout.json").write_text(completed.stdout, encoding="utf-8")
        (attempt_dir / "openclaw_stderr.txt").write_text(completed.stderr, encoding="utf-8")
        payload = parse_openclaw_json(completed.stdout)
        response_text = extract_response_text(payload)
        meta = payload.get("meta", {}) if isinstance(payload, dict) else {}
        agent_meta = meta.get("agentMeta", {}) if isinstance(meta, dict) else {}
        usage = agent_meta.get("usage", {}) if isinstance(agent_meta, dict) else {}
        marker_created = marker_path.exists()
        marker_content = marker_path.read_text(errors="replace") if marker_created else ""
        marker_content_ok = marker_content == marker_token
        output_mentions_marker = marker_token in response_text
        status = "pass" if completed.returncode == 0 and marker_content_ok else "fail"
        error_tail = tail(completed.stderr + "\n" + completed.stdout)
        return NativeToolResult(
            model_id=model_id,
            rank=rank,
            provider_id=provider_id,
            port=port,
            status=status,
            marker_created=marker_created,
            marker_content_ok=marker_content_ok,
            output_mentions_marker=output_mentions_marker,
            duration_seconds=round(time.perf_counter() - start, 3),
            server_start_seconds=server_start_seconds,
            openclaw_returncode=completed.returncode,
            prompt_tokens=int_or_none(usage.get("input")),
            output_tokens=int_or_none(usage.get("output")),
            cache_read_tokens=int_or_none(usage.get("cacheRead")),
            compaction_count=int_or_none(agent_meta.get("compactionCount")),
            response_text=response_text,
            error_tail=error_tail,
            server_log=tail(server_log_path.read_text(errors="replace")),
            cache_bytes_before_cleanup=directory_size(cache_dir),
            cleanup_status=cleanup_cache(cache_dir, keep_cache),
        )
    except Exception as exc:  # noqa: BLE001
        return NativeToolResult(
            model_id=model_id,
            rank=rank,
            provider_id=provider_id,
            port=port,
            status="error",
            marker_created=marker_path.exists(),
            marker_content_ok=False,
            output_mentions_marker=False,
            duration_seconds=round(time.perf_counter() - start, 3),
            server_start_seconds=round(time.perf_counter() - server_start, 3),
            openclaw_returncode=None,
            prompt_tokens=None,
            output_tokens=None,
            cache_read_tokens=None,
            compaction_count=None,
            response_text="",
            error_tail=repr(exc),
            server_log=tail(server_log_path.read_text(errors="replace")) if server_log_path.exists() else "",
            cache_bytes_before_cleanup=directory_size(cache_dir),
            cleanup_status=cleanup_cache(cache_dir, keep_cache),
        )
    finally:
        if server_proc and server_proc.poll() is None:
            server_proc.terminate()
            try:
                server_proc.wait(timeout=20)
            except subprocess.TimeoutExpired:
                server_proc.kill()
                server_proc.wait(timeout=20)
        log_handle.close()


def wait_ready(port: int, proc: subprocess.Popen[bytes], timeout: int) -> None:
    deadline = time.time() + timeout
    url = f"http://127.0.0.1:{port}/v1/models"
    last_error = "not attempted"
    while time.time() < deadline:
        if proc.poll() is not None:
            raise RuntimeError(f"mlx server exited early rc={proc.returncode}")
        try:
            with urlopen(url, timeout=2) as response:
                if response.status == 200:
                    return
        except URLError as exc:
            last_error = repr(exc)
        except TimeoutError as exc:
            last_error = repr(exc)
        time.sleep(1)
    raise TimeoutError(f"server not ready at {url}: {last_error}")


def warm_model(port: int, model_id: str, timeout: int) -> None:
    """Force first model load/download before the OpenClaw agent timeout starts."""
    payload = {
        "model": model_id,
        "messages": [{"role": "user", "content": "Reply with ok."}],
        "max_tokens": 1,
        "temperature": 0,
    }
    request = Request(
        f"http://127.0.0.1:{port}/v1/chat/completions",
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json", "Authorization": "Bearer local"},
    )
    with urlopen(request, timeout=timeout) as response:
        if response.status != 200:
            raise RuntimeError(f"warmup failed status={response.status}")


def write_temp_openclaw_config(provider_id: str, model_id: str, port: int, max_tokens: int) -> Path:
    data = json.loads(OPENCLAW_CONFIG.read_text())
    key = f"{provider_id}/{model_id}"
    data.setdefault("models", {}).setdefault("providers", {})[provider_id] = {
        "baseUrl": f"http://127.0.0.1:{port}/v1",
        "apiKey": "local",
        "api": "openai-completions",
        "contextWindow": 32768,
        "contextTokens": 32768,
        "maxTokens": max_tokens,
        "timeoutSeconds": 300,
        "injectNumCtxForOpenAICompat": False,
        "models": [
            {
                "id": model_id,
                "name": f"{model_id} OpenClaw native tool canary",
                "reasoning": False,
                "input": ["text"],
                "cost": {"input": 0, "output": 0, "cacheRead": 0, "cacheWrite": 0},
                "contextWindow": 32768,
                "contextTokens": 32768,
                "maxTokens": max_tokens,
                "compat": {"supportsTools": True},
            }
        ],
    }
    agents = data.setdefault("agents", {})
    defaults = agents.setdefault("defaults", {})
    defaults["model"] = {"primary": key, "fallbacks": []}
    defaults.setdefault("compaction", {})["reserveTokensFloor"] = 1024
    defaults.setdefault("models", {})[key] = {"streaming": False}
    for agent in agents.get("list", []):
        if agent.get("id") == "main":
            agent["model"] = key
            agent.setdefault("models", {})[key] = {"streaming": False}
            break
    handle = tempfile.NamedTemporaryFile("w", suffix=".json", prefix="openclaw-native-tools-", delete=False)
    with handle:
        json.dump(data, handle, indent=2)
    return Path(handle.name)


def parse_openclaw_json(stdout: str) -> dict[str, object]:
    try:
        return json.loads(stdout)
    except json.JSONDecodeError:
        start = stdout.find("{")
        end = stdout.rfind("}")
        if start >= 0 and end > start:
            return json.loads(stdout[start : end + 1])
    return {}


def extract_response_text(payload: dict[str, object]) -> str:
    payloads = payload.get("payloads", [])
    if isinstance(payloads, list):
        return "\n".join(str(item.get("text", "")) for item in payloads if isinstance(item, dict))
    return ""


def int_or_none(value: object) -> int | None:
    try:
        return int(value)  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return None


def cleanup_cache(cache_dir: Path, keep_cache: bool) -> str:
    if keep_cache:
        return "kept"
    try:
        shutil.rmtree(cache_dir)
        return "deleted"
    except Exception as exc:  # noqa: BLE001
        return f"failed:{exc!r}"


def write_reports(summary_path: Path, report_json: Path, report_md: Path) -> None:
    rows = load_existing(summary_path)
    rows.sort(key=lambda item: int(item.get("rank", 999)))
    totals = {
        "count": len(rows),
        "pass_count": sum(1 for item in rows if item.get("status") == "pass"),
        "fail_count": sum(1 for item in rows if item.get("status") == "fail"),
        "error_count": sum(1 for item in rows if item.get("status") == "error"),
    }
    report_json.write_text(json.dumps({"summary": totals, "results": rows}, indent=2, ensure_ascii=False))
    lines = [
        "# OpenClaw Native Tool Execution Suite - 2026-05-31",
        "",
        "This suite checks whether each MLX model can drive OpenClaw's actual native tool loop.",
        "Pass means the model caused OpenClaw to execute the `exec` tool and create a nonce marker file.",
        "",
        f"Summary: {totals['pass_count']}/{totals['count']} pass, {totals['fail_count']} fail, {totals['error_count']} error.",
        "",
        "| Rank | Model | Status | Marker | Duration | Prompt toks | Output toks | Compactions |",
        "| ---: | --- | --- | --- | ---: | ---: | ---: | ---: |",
    ]
    for item in rows:
        marker = "yes" if item.get("marker_content_ok") else "no"
        lines.append(
            f"| {item.get('rank')} | `{item.get('model_id')}` | `{item.get('status')}` | {marker} | "
            f"{item.get('duration_seconds')}s | {item.get('prompt_tokens')} | {item.get('output_tokens')} | "
            f"{item.get('compaction_count')} |"
        )
    lines.extend(["", "## Notes", ""])
    for item in rows:
        text = str(item.get("response_text", "")).replace("\n", " ")
        if not text:
            text = str(item.get("error_tail", "")).replace("\n", " ")
        if len(text) > 240:
            text = text[:237] + "..."
        lines.append(f"- `{item.get('model_id')}`: {text}")
    report_md.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    raise SystemExit(main())
