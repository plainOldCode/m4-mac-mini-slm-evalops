from __future__ import annotations

import argparse
from pathlib import Path

from .backends import get_backend
from .harness import run_attempt


def main() -> int:
    parser = argparse.ArgumentParser(prog="llm-evalops")
    subparsers = parser.add_subparsers(dest="command", required=True)

    run_parser = subparsers.add_parser("run", help="Run one isolated task attempt")
    run_parser.add_argument("--task", required=True, type=Path)
    run_parser.add_argument(
        "--backend",
        required=True,
        choices=[
            "noop",
            "scripted",
        ],
    )
    run_parser.add_argument("--runs-dir", required=True, type=Path)
    run_parser.add_argument("--attempt-id", type=int, default=1)

    args = parser.parse_args()
    if args.command == "run":
        report = run_attempt(args.task, get_backend(args.backend), args.runs_dir, args.attempt_id)
        status = "PASS" if report.tests_passed else "FAIL"
        print(f"{status} task={report.task} backend={report.backend} changed={report.changed} diff_lines={report.diff_lines}")
        print(args.runs_dir / f"attempt-{args.attempt_id:04d}" / "report.json")
        return 0 if report.tests_passed else 1
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
