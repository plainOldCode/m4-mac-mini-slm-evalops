from __future__ import annotations

import difflib
import json
import shutil
import subprocess
import time
from dataclasses import asdict, dataclass
from pathlib import Path

from .backends import Backend
from .tasks import TaskSpec, load_task


@dataclass(frozen=True)
class AttemptReport:
    task: str
    backend: str
    attempt_id: int
    changed: bool
    tests_passed: bool
    returncode: int
    elapsed_seconds: float
    diff_lines: int
    stdout_tail: str
    stderr_tail: str
    backend_message: str


def run_attempt(task_dir: Path, backend: Backend, runs_dir: Path, attempt_id: int = 1) -> AttemptReport:
    task = load_task(task_dir)
    attempt_dir = runs_dir / f"attempt-{attempt_id:04d}"
    attempt_repo = attempt_dir / "repo"

    if attempt_dir.exists():
        shutil.rmtree(attempt_dir)
    attempt_dir.mkdir(parents=True)
    shutil.copytree(task_dir / "repo", attempt_repo)

    before = snapshot_files(attempt_repo)
    start = time.perf_counter()
    backend_result = backend.run(task_dir, attempt_repo)
    completed = subprocess.run(
        task.test_command,
        cwd=attempt_repo,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        timeout=60,
    )
    elapsed = time.perf_counter() - start
    after = snapshot_files(attempt_repo)
    diff_text = build_diff(before, after)

    (attempt_dir / "diff.patch").write_text(diff_text)
    (attempt_dir / "stdout.txt").write_text(completed.stdout)
    (attempt_dir / "stderr.txt").write_text(completed.stderr)

    report = AttemptReport(
        task=task.name,
        backend=backend.name,
        attempt_id=attempt_id,
        changed=backend_result.changed,
        tests_passed=completed.returncode == 0,
        returncode=completed.returncode,
        elapsed_seconds=round(elapsed, 3),
        diff_lines=len(diff_text.splitlines()),
        stdout_tail=tail(completed.stdout),
        stderr_tail=tail(completed.stderr),
        backend_message=backend_result.message,
    )
    (attempt_dir / "report.json").write_text(json.dumps(asdict(report), indent=2, ensure_ascii=False))
    update_index(runs_dir, report)
    return report


def snapshot_files(root: Path) -> dict[str, str]:
    files: dict[str, str] = {}
    for path in sorted(root.rglob("*")):
        if path.is_file() and should_snapshot(path):
            files[str(path.relative_to(root))] = path.read_text(errors="replace")
    return files


def should_snapshot(path: Path) -> bool:
    if "__pycache__" in path.parts:
        return False
    if path.suffix in {".pyc", ".pyo"}:
        return False
    return True


def build_diff(before: dict[str, str], after: dict[str, str]) -> str:
    chunks: list[str] = []
    for name in sorted(set(before) | set(after)):
        old = before.get(name, "").splitlines(keepends=True)
        new = after.get(name, "").splitlines(keepends=True)
        if old == new:
            continue
        chunks.extend(difflib.unified_diff(old, new, fromfile=f"a/{name}", tofile=f"b/{name}"))
    return "".join(chunks)


def tail(text: str, max_chars: int = 2000) -> str:
    return text[-max_chars:]


def update_index(runs_dir: Path, report: AttemptReport) -> None:
    index_path = runs_dir / "index.json"
    if index_path.exists():
        data = json.loads(index_path.read_text())
    else:
        data = {"attempts": []}
    data["attempts"].append(asdict(report))
    index_path.write_text(json.dumps(data, indent=2, ensure_ascii=False))
