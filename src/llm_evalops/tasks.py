from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class TaskSpec:
    name: str
    description: str
    test_command: list[str]
    allowed_paths: list[str]


def load_task(task_dir: Path) -> TaskSpec:
    data = json.loads((task_dir / "task.json").read_text())
    return TaskSpec(
        name=data["name"],
        description=data.get("description", ""),
        test_command=list(data["test_command"]),
        allowed_paths=list(data.get("allowed_paths", [])),
    )
