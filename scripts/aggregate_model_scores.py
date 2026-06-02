#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


DEFAULT_REPORT_JSON = Path("reports/small-models/aggregate-model-scores.json")
DEFAULT_REPORT_MD = Path("reports/small-models/aggregate-model-scores.md")


def main() -> int:
    parser = argparse.ArgumentParser(description="Aggregate model scores across quality, protocol, and hardware lanes.")
    parser.add_argument("--factual-report", type=Path)
    parser.add_argument("--tool-report", type=Path)
    parser.add_argument("--native-report", type=Path)
    parser.add_argument("--coding-report", type=Path)
    parser.add_argument("--report-json", type=Path, default=DEFAULT_REPORT_JSON)
    parser.add_argument("--report-md", type=Path, default=DEFAULT_REPORT_MD)
    args = parser.parse_args()

    output = aggregate_reports(
        factual=load_json(args.factual_report),
        tool=load_json(args.tool_report),
        native=load_json(args.native_report),
        coding=load_json(args.coding_report),
    )
    args.report_json.parent.mkdir(parents=True, exist_ok=True)
    args.report_md.parent.mkdir(parents=True, exist_ok=True)
    args.report_json.write_text(json.dumps(output, indent=2, ensure_ascii=False))
    args.report_md.write_text(render_markdown(output))
    print(f"Wrote {args.report_json}")
    print(f"Wrote {args.report_md}")
    return 0


def load_json(path: Path | None) -> dict[str, Any] | None:
    if path is None:
        return None
    return json.loads(path.read_text())


def aggregate_reports(
    factual: dict[str, Any] | None = None,
    tool: dict[str, Any] | None = None,
    native: dict[str, Any] | None = None,
    coding: dict[str, Any] | None = None,
) -> dict[str, Any]:
    rows: dict[str, dict[str, Any]] = {}

    for model in (factual or {}).get("models", []):
        row = ensure_row(rows, model["model_id"])
        add_component(row, "quality", "factual_alias", pct(model.get("alias_normalized_match_count"), model.get("prompt_count")))
        add_component(row, "quality", "factual_strict", pct(model.get("strict_canonical_match_count"), model.get("prompt_count")))
        add_component(row, "protocol", "factual_json", pct(model.get("json_valid_count"), model.get("prompt_count")))
        add_component(row, "protocol", "factual_schema", pct(model.get("schema_valid_count"), model.get("prompt_count")))

    for model in (tool or {}).get("models", []):
        row = ensure_row(rows, model["model_id"])
        add_component(row, "protocol", "tool_case_pass", pct(model.get("case_pass_count"), model.get("case_count")))
        add_component(row, "protocol", "tool_sequence", pct(model.get("tool_sequence_match_count"), model.get("case_count")))
        add_component(row, "protocol", "tool_arguments", pct(model.get("arguments_match_count"), model.get("case_count")))
        add_component(row, "hardware", "tool_completion", status_score(model.get("download_status")))
        add_component(row, "hardware", "tool_elapsed", elapsed_score(model.get("elapsed_seconds")))
        add_component(row, "hardware", "tool_cleanup", cleanup_score(model.get("cleanup_status")))

    for model in (native or {}).get("results", []):
        row = ensure_row(rows, model["model_id"])
        add_component(row, "protocol", "native_tool", 100.0 if model.get("status") == "pass" else 0.0)
        add_component(row, "hardware", "native_elapsed", elapsed_score(model.get("duration_seconds")))
        add_component(row, "hardware", "native_cleanup", cleanup_score(model.get("cleanup_status")))

    for model in (coding or {}).get("models", []):
        row = ensure_row(rows, model["model_id"])
        add_component(row, "quality", "coding_tests", pct(model.get("tests_passed_count"), model.get("task_count")))
        add_component(row, "protocol", "coding_json", pct(model.get("json_valid_count"), model.get("task_count")))
        add_component(row, "protocol", "coding_schema", pct(model.get("schema_valid_count"), model.get("task_count")))
        add_component(row, "hardware", "coding_completion", status_score(model.get("download_status")))
        add_component(row, "hardware", "coding_elapsed", elapsed_score(model.get("elapsed_seconds")))
        add_component(row, "hardware", "coding_cleanup", cleanup_score(model.get("cleanup_status")))

    models = [finalize_row(row) for row in rows.values()]
    models.sort(
        key=lambda row: (
            row["aggregate_score"],
            row["quality_score"],
            row["protocol_score"],
            row["hardware_score"],
        ),
        reverse=True,
    )
    for rank, row in enumerate(models, start=1):
        row["rank"] = rank

    return {
        "suite": "aggregate-model-scores",
        "method": "Aggregate = 45% quality + 35% protocol + 20% hardware. Each dimension averages available components only.",
        "models": models,
    }


def ensure_row(rows: dict[str, dict[str, Any]], model_id: str) -> dict[str, Any]:
    if model_id not in rows:
        rows[model_id] = {
            "model_id": model_id,
            "components": {
                "quality": {},
                "protocol": {},
                "hardware": {},
            },
        }
    return rows[model_id]


def add_component(row: dict[str, Any], dimension: str, name: str, value: float | None) -> None:
    if value is None:
        return
    row["components"][dimension][name] = round(value, 1)


def finalize_row(row: dict[str, Any]) -> dict[str, Any]:
    quality = average(row["components"]["quality"].values())
    protocol = average(row["components"]["protocol"].values())
    hardware = average(row["components"]["hardware"].values())
    aggregate = (quality * 0.45) + (protocol * 0.35) + (hardware * 0.20)
    return {
        "model_id": row["model_id"],
        "aggregate_score": round(aggregate, 1),
        "quality_score": round(quality, 1),
        "protocol_score": round(protocol, 1),
        "hardware_score": round(hardware, 1),
        "components": row["components"],
    }


def pct(numerator: Any, denominator: Any) -> float | None:
    try:
        numerator_float = float(numerator)
        denominator_float = float(denominator)
    except (TypeError, ValueError):
        return None
    if denominator_float <= 0:
        return None
    return (numerator_float / denominator_float) * 100.0


def average(values: Any) -> float:
    numbers = [float(value) for value in values]
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)


def status_score(status: Any) -> float | None:
    if status is None:
        return None
    return 100.0 if str(status) == "ok" else 0.0


def cleanup_score(status: Any) -> float | None:
    if status is None:
        return None
    return 100.0 if str(status) in {"ok", "not_required"} else 0.0


def elapsed_score(seconds: Any) -> float | None:
    try:
        value = float(seconds)
    except (TypeError, ValueError):
        return None
    if value <= 60:
        return 100.0
    if value <= 120:
        return 80.0
    if value <= 240:
        return 60.0
    if value <= 600:
        return 40.0
    return 20.0


def render_markdown(output: dict[str, Any]) -> str:
    lines = [
        "# Aggregate Model Scores",
        "",
        output["method"],
        "",
        "| Rank | Model | Aggregate | Quality | Protocol | Hardware |",
        "| ---: | --- | ---: | ---: | ---: | ---: |",
    ]
    for model in output["models"]:
        lines.append(
            f"| {model['rank']} | `{model['model_id']}` | "
            f"{model['aggregate_score']:.1f} | {model['quality_score']:.1f} | "
            f"{model['protocol_score']:.1f} | {model['hardware_score']:.1f} |"
        )
    lines.append("")
    return "\n".join(lines)


if __name__ == "__main__":
    raise SystemExit(main())
