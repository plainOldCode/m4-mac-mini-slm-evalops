from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "aggregate_model_scores.py"
spec = importlib.util.spec_from_file_location("aggregate_model_scores", SCRIPT)
assert spec is not None
module = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules[spec.name] = module
spec.loader.exec_module(module)


class AggregateModelScoresTest(unittest.TestCase):
    def test_aggregate_prefers_balanced_quality_protocol_hardware(self) -> None:
        factual = {
            "models": [
                {
                    "model_id": "model-a",
                    "prompt_count": 100,
                    "alias_normalized_match_count": 90,
                    "strict_canonical_match_count": 70,
                    "json_valid_count": 100,
                    "schema_valid_count": 100,
                },
                {
                    "model_id": "model-b",
                    "prompt_count": 100,
                    "alias_normalized_match_count": 95,
                    "strict_canonical_match_count": 80,
                    "json_valid_count": 90,
                    "schema_valid_count": 90,
                },
            ]
        }
        tool = {
            "models": [
                {
                    "model_id": "model-a",
                    "case_count": 12,
                    "case_pass_count": 9,
                    "tool_sequence_match_count": 10,
                    "arguments_match_count": 9,
                    "download_status": "ok",
                    "elapsed_seconds": 55,
                    "cleanup_status": "ok",
                },
                {
                    "model_id": "model-b",
                    "case_count": 12,
                    "case_pass_count": 4,
                    "tool_sequence_match_count": 4,
                    "arguments_match_count": 4,
                    "download_status": "ok",
                    "elapsed_seconds": 700,
                    "cleanup_status": "failed",
                },
            ]
        }

        output = module.aggregate_reports(factual=factual, tool=tool)

        self.assertEqual(output["models"][0]["model_id"], "model-a")
        self.assertEqual(output["models"][0]["quality_score"], 80.0)
        self.assertEqual(output["models"][0]["hardware_score"], 100.0)
        self.assertLess(output["models"][1]["hardware_score"], output["models"][0]["hardware_score"])

    def test_native_and_coding_components_are_included(self) -> None:
        native = {
            "results": [
                {
                    "model_id": "model-a",
                    "status": "pass",
                    "duration_seconds": 30,
                    "cleanup_status": "not_required",
                }
            ]
        }
        coding = {
            "models": [
                {
                    "model_id": "model-a",
                    "task_count": 5,
                    "tests_passed_count": 4,
                    "json_valid_count": 5,
                    "schema_valid_count": 5,
                    "download_status": "ok",
                    "elapsed_seconds": 100,
                    "cleanup_status": "ok",
                }
            ]
        }

        output = module.aggregate_reports(native=native, coding=coding)
        model = output["models"][0]

        self.assertEqual(model["components"]["protocol"]["native_tool"], 100.0)
        self.assertEqual(model["components"]["quality"]["coding_tests"], 80.0)
        self.assertEqual(model["components"]["hardware"]["coding_elapsed"], 80.0)


if __name__ == "__main__":
    unittest.main()
