from __future__ import annotations

import shutil
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


def get_backend(name: str) -> Backend:
    backends: dict[str, Backend] = {
        NoopBackend.name: NoopBackend(),
        ScriptedSolutionBackend.name: ScriptedSolutionBackend(),
    }
    try:
        return backends[name]
    except KeyError as exc:
        available = ", ".join(sorted(backends))
        raise ValueError(f"unknown backend {name!r}; available: {available}") from exc
