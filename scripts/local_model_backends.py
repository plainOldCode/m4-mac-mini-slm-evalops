from __future__ import annotations

import json
import subprocess
import time
import urllib.request
import urllib.error


def backend_of(candidate: dict[str, str]) -> str:
    return candidate.get("backend", "mlx")


def decode_maybe(value: str | bytes | None) -> str:
    if value is None:
        return ""
    if isinstance(value, bytes):
        return value.decode("utf-8", errors="replace")
    return value


def tail(text: str, limit: int = 1200) -> str:
    if len(text) <= limit:
        return text
    return text[-limit:]


def pull_ollama_model(model_id: str, timeout: int) -> tuple[str, float, str, str]:
    start = time.perf_counter()
    command = ["ollama", "pull", model_id]
    try:
        completed = subprocess.run(
            command,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=timeout,
        )
        status = "ok" if completed.returncode == 0 else "failed"
        return status, round(time.perf_counter() - start, 3), completed.stdout or "", completed.stderr or ""
    except subprocess.TimeoutExpired as exc:
        return "timeout", round(time.perf_counter() - start, 3), decode_maybe(exc.stdout), decode_maybe(exc.stderr)
    except Exception as exc:  # noqa: BLE001
        return "error", round(time.perf_counter() - start, 3), "", repr(exc)


def remove_ollama_model(model_id: str, timeout: int = 120) -> tuple[str, str]:
    try:
        completed = subprocess.run(
            ["ollama", "rm", model_id],
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=timeout,
        )
        status = "deleted" if completed.returncode == 0 else "failed"
        return status, (completed.stdout or "") + (completed.stderr or "")
    except subprocess.TimeoutExpired as exc:
        return "timeout", decode_maybe(exc.stdout) + decode_maybe(exc.stderr)
    except Exception as exc:  # noqa: BLE001
        return "error", repr(exc)


def generate_ollama(model_id: str, prompt: str, timeout: int, max_tokens: int) -> tuple[str, str, str]:
    effective_prompt = prompt
    if model_id.lower().startswith("qwen3") and "/no_think" not in prompt:
        effective_prompt = "/no_think\n" + prompt
    payload = {
        "model": model_id,
        "prompt": effective_prompt,
        "stream": False,
        "think": False,
        "format": "json",
        "options": {
            "temperature": 0,
            "num_predict": max_tokens,
        },
    }
    request = urllib.request.Request(
        "http://127.0.0.1:11434/api/generate",
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:  # noqa: S310
            data = json.loads(response.read().decode("utf-8"))
        text = str(data.get("response", ""))
        status = "ok" if text.strip() else "failed"
        stderr = "" if status == "ok" else tail(json.dumps(data, ensure_ascii=False))
        return text, status, stderr
    except urllib.error.URLError as exc:
        return "", "error", tail(repr(exc))
    except TimeoutError as exc:
        return "", "timeout", tail(repr(exc))
    except Exception as exc:  # noqa: BLE001
        return "", "error", tail(repr(exc))
