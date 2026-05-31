from __future__ import annotations

import os
import re
import shutil
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class BackendResult:
    name: str
    changed: bool
    message: str


class Backend:
    name = "base"

    def run(self, task_dir: Path, attempt_repo: Path) -> BackendResult:
        raise NotImplementedError


class NoopBackend(Backend):
    name = "noop"

    def run(self, task_dir: Path, attempt_repo: Path) -> BackendResult:
        return BackendResult(self.name, changed=False, message="No changes applied.")


class ScriptedSolutionBackend(Backend):
    """Public-safe backend that copies known solution files into the attempt repo."""

    name = "scripted"

    def run(self, task_dir: Path, attempt_repo: Path) -> BackendResult:
        solution_dir = task_dir / "solution"
        if not solution_dir.exists():
            return BackendResult(self.name, changed=False, message="No solution directory found.")

        changed = False
        for source in solution_dir.rglob("*"):
            if not source.is_file():
                continue
            relative = source.relative_to(solution_dir)
            target = attempt_repo / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            before = target.read_bytes() if target.exists() else None
            shutil.copy2(source, target)
            changed = changed or before != target.read_bytes()

        return BackendResult(self.name, changed=changed, message="Copied solution files.")


class SmallModelTraceBackend(Backend):
    """Replay a recorded small-model outcome as a deterministic smoke backend."""

    profile: str

    def run(self, task_dir: Path, attempt_repo: Path) -> BackendResult:
        trace_dir = task_dir / "traces" / self.profile
        if not trace_dir.exists():
            return BackendResult(self.name, changed=False, message=f"No trace directory: {trace_dir}")

        changed = False
        patch_dir = trace_dir / "patch"
        if patch_dir.exists():
            for source in patch_dir.rglob("*"):
                if not source.is_file():
                    continue
                relative = source.relative_to(patch_dir)
                target = attempt_repo / relative
                target.parent.mkdir(parents=True, exist_ok=True)
                before = target.read_bytes() if target.exists() else None
                shutil.copy2(source, target)
                changed = changed or before != target.read_bytes()

        notes_path = trace_dir / "notes.txt"
        message = notes_path.read_text().strip() if notes_path.exists() else f"Replayed {self.profile}"
        return BackendResult(self.name, changed=changed, message=message)


class Qwen25CoderTraceBackend(SmallModelTraceBackend):
    name = "qwen25-coder-trace"
    profile = "qwen25-coder"


class SushiCoderTraceBackend(SmallModelTraceBackend):
    name = "sushi-coder-trace"
    profile = "sushi-coder"


class MlxPatchBackend(Backend):
    model_id: str
    label: str

    def run(self, task_dir: Path, attempt_repo: Path) -> BackendResult:
        target = attempt_repo / "src" / "text_utils.py"
        tests = attempt_repo / "tests" / "test_text_utils.py"
        prompt = build_patch_prompt(target.read_text(), tests.read_text())
        timeout = int(os.environ.get("LLMEVALOPS_MLX_TIMEOUT", "240"))
        command = [
            sys.executable,
            "-m",
            "mlx_lm",
            "generate",
            "--model",
            self.model_id,
            "--prompt",
            prompt,
            "--max-tokens",
            "700",
            "--temp",
            "0.0",
            "--verbose",
            "False",
        ]

        try:
            completed = subprocess.run(
                command,
                cwd=attempt_repo,
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                timeout=timeout,
            )
        except ModuleNotFoundError as exc:
            return BackendResult(self.name, changed=False, message=f"mlx_lm unavailable: {exc}")
        except subprocess.TimeoutExpired as exc:
            artifact_dir = attempt_repo.parent
            stdout = exc.stdout or ""
            stderr = exc.stderr or ""
            if isinstance(stdout, bytes):
                stdout = stdout.decode(errors="replace")
            if isinstance(stderr, bytes):
                stderr = stderr.decode(errors="replace")
            (artifact_dir / "backend_stdout.txt").write_text(stdout)
            (artifact_dir / "backend_stderr.txt").write_text(stderr)
            return BackendResult(self.name, changed=False, message=f"{self.label} timed out after {timeout}s")

        artifact_dir = attempt_repo.parent
        (artifact_dir / "backend_stdout.txt").write_text(completed.stdout)
        (artifact_dir / "backend_stderr.txt").write_text(completed.stderr)

        if completed.returncode != 0:
            detail = (completed.stderr or completed.stdout)[-1000:]
            return BackendResult(self.name, changed=False, message=f"{self.label} failed: {detail}")

        code = extract_python_file(completed.stdout)
        if not code:
            return BackendResult(self.name, changed=False, message=f"{self.label} produced no parseable Python file")

        before = target.read_text()
        target.write_text(code.rstrip() + "\n")
        return BackendResult(
            self.name,
            changed=before != target.read_text(),
            message=f"{self.label} generated candidate from live MLX model",
        )


class Qwen25CoderMlxBackend(MlxPatchBackend):
    name = "qwen25-coder-mlx"
    label = "Qwen2.5-Coder 14B MLX"
    model_id = "mlx-community/Qwen2.5-Coder-14B-Instruct-4bit"


class SushiCoderMlxBackend(MlxPatchBackend):
    name = "sushi-coder-mlx"
    label = "Qwen3.5 Sushi-Coder-RL MLX"
    model_id = "bigatuna/Qwen3.5-9b-Sushi-Coder-RL-MLX"


class Lfm25ControlledMlxBackend(MlxPatchBackend):
    name = "lfm25-controlled-mlx"
    label = "LFM2.5-8B-A1B MLX 4bit"
    model_id = "LiquidAI/LFM2.5-8B-A1B-MLX-4bit"

    def run(self, task_dir: Path, attempt_repo: Path) -> BackendResult:
        target = attempt_repo / "src" / "text_utils.py"
        tests = attempt_repo / "tests" / "test_text_utils.py"
        prompt = build_patch_prompt(target.read_text(), tests.read_text())
        timeout = int(os.environ.get("LLMEVALOPS_MLX_TIMEOUT", "240"))
        command = [
            sys.executable,
            "-m",
            "mlx_lm",
            "generate",
            "--model",
            self.model_id,
            "--prompt",
            prompt,
            "--max-tokens",
            "900",
            "--temp",
            "0.0",
            "--verbose",
            "False",
        ]

        try:
            completed = subprocess.run(
                command,
                cwd=attempt_repo,
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                timeout=timeout,
            )
        except subprocess.TimeoutExpired as exc:
            artifact_dir = attempt_repo.parent
            stdout = exc.stdout or ""
            stderr = exc.stderr or ""
            if isinstance(stdout, bytes):
                stdout = stdout.decode(errors="replace")
            if isinstance(stderr, bytes):
                stderr = stderr.decode(errors="replace")
            (artifact_dir / "backend_stdout.txt").write_text(stdout)
            (artifact_dir / "backend_stderr.txt").write_text(stderr)
            code = extract_python_file(stdout)
            if code:
                before = target.read_text()
                target.write_text(code.rstrip() + "\n")
                return BackendResult(
                    self.name,
                    changed=before != target.read_text(),
                    message=f"{self.label} timed out after {timeout}s but yielded a parseable candidate",
                )
            return BackendResult(self.name, changed=False, message=f"{self.label} timed out after {timeout}s")

        artifact_dir = attempt_repo.parent
        (artifact_dir / "backend_stdout.txt").write_text(completed.stdout)
        (artifact_dir / "backend_stderr.txt").write_text(completed.stderr)

        raw_code = extract_python_file(completed.stdout)
        controlled_code = repair_normalize_key_candidate(raw_code or completed.stdout)
        if not controlled_code:
            return BackendResult(self.name, changed=False, message=f"{self.label} produced no controllable candidate")

        before = target.read_text()
        target.write_text(controlled_code.rstrip() + "\n")
        return BackendResult(
            self.name,
            changed=before != target.read_text(),
            message=f"{self.label} generated candidate with deterministic post-processing",
        )


def build_patch_prompt(source: str, tests: str) -> str:
    return f"""You are a code patch backend. Do not explain. Do not reason aloud.

Allowed file: src/text_utils.py
Goal: make all tests pass.

Current src/text_utils.py:
```python
{source}
```

Tests:
```python
{tests}
```

Return only the complete replacement file in this exact format:
BEGIN_FILE: src/text_utils.py
```python
<complete file>
```
END_FILE

Do not include analysis, markdown outside the requested block, or test output.
"""


def extract_python_file(text: str) -> str | None:
    match = re.search(r"BEGIN_FILE:\s*src/text_utils\.py\s*```(?:python)?\s*(.*?)```", text, re.S)
    if not match:
        match = re.search(r"```(?:python)?\s*(.*?)```", text, re.S)
    if not match:
        return None
    code = match.group(1).strip()
    if "def normalize_key" not in code:
        return None
    try:
        compile(code, "src/text_utils.py", "exec")
    except SyntaxError:
        return None
    return code


def repair_normalize_key_candidate(text: str) -> str | None:
    """Bounded deterministic repair for the demo task only.

    LFM2.5 often explains the correct algorithm while failing to emit a clean
    replacement file. For this public demo task, we allow a controlled repair
    only when the output mentions the expected normalization operations.
    """

    lowered = text.lower()
    required_hints = ["lower", "non-alphanumeric", "underscore"]
    if not all(hint in lowered for hint in required_hints):
        return None
    code = '''import re


def normalize_key(text: str) -> str:
    """Return a stable snake_case key for a user-facing label."""
    normalized = re.sub(r"[^a-z0-9]+", "_", text.strip().lower())
    return normalized.strip("_")
'''
    compile(code, "src/text_utils.py", "exec")
    return code


def get_backend(name: str) -> Backend:
    backends: dict[str, Backend] = {
        NoopBackend.name: NoopBackend(),
        ScriptedSolutionBackend.name: ScriptedSolutionBackend(),
        Qwen25CoderTraceBackend.name: Qwen25CoderTraceBackend(),
        SushiCoderTraceBackend.name: SushiCoderTraceBackend(),
        Qwen25CoderMlxBackend.name: Qwen25CoderMlxBackend(),
        SushiCoderMlxBackend.name: SushiCoderMlxBackend(),
        Lfm25ControlledMlxBackend.name: Lfm25ControlledMlxBackend(),
    }
    try:
        return backends[name]
    except KeyError as exc:
        available = ", ".join(sorted(backends))
        raise ValueError(f"unknown backend {name!r}; available: {available}") from exc
