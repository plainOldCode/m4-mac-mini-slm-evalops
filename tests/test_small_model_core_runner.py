from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parents[1] / "scripts"
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

SCRIPT = SCRIPT_DIR / "run_small_model_core_suite.py"
spec = importlib.util.spec_from_file_location("run_small_model_core_suite", SCRIPT)
assert spec is not None
module = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules[spec.name] = module
spec.loader.exec_module(module)


def make_case(lane: str, expected: dict, **kwargs):
    return module.CoreCase(
        index=1,
        lane=lane,
        case_id=kwargs.get("case_id", "case-001"),
        title="Case",
        prompt="Return JSON only.",
        expected=expected,
        fixture_dir="",
        solution_dir="",
        allowed_paths=kwargs.get("allowed_paths", []),
    )


class SmallModelCoreRunnerTest(unittest.TestCase):
    def test_scores_summary_contains_and_list_fields(self) -> None:
        case = make_case(
            "summary",
            {
                "winner": "Qwen3 4B",
                "risks": ["tool selection score was 7 of 12"],
                "recommendation_contains": ["OpenClaw"],
            },
        )
        parsed = {
            "case_id": "case-001",
            "answer": {
                "winner": "Qwen3 4B",
                "risks": ["The tool selection score was 7 of 12."],
                "recommendation": "Keep as practical OpenClaw candidate.",
            },
        }

        self.assertEqual(module.score_case(parsed, case), {"schema_valid": True, "content_match": True, "case_pass": True})

    def test_scores_protocol_sequence_and_argument_substrings(self) -> None:
        case = make_case(
            "protocol",
            {
                "tool_sequence": ["web_search", "calculator"],
                "search_query_contains": ["USD", "KRW"],
                "calculator_expression_contains": ["250"],
            },
        )
        parsed = {
            "tool_calls": [
                {"tool_name": "web_search", "arguments": {"query": "current USD KRW exchange rate"}},
                {"tool_name": "calculator", "arguments": {"expression": "250 * USD_KRW"}},
            ]
        }

        self.assertIs(module.score_case(parsed, case)["case_pass"], True)

    def test_scores_patch_allowlisted_replacement_content(self) -> None:
        case = make_case(
            "patch",
            {
                "contains": ["Qwen3 4B remains the lightweight local baseline."],
                "does_not_contain": ["PRIVATE"],
            },
            allowed_paths=["README.md"],
        )
        parsed = {
            "case_id": "case-001",
            "files": [{"path": "README.md", "content": "# Model Card\n\nQwen3 4B remains the lightweight local baseline.\n"}],
        }

        self.assertEqual(module.score_case(parsed, case), {"schema_valid": True, "content_match": True, "case_pass": True})

    def test_rejects_patch_outside_allowlist(self) -> None:
        case = make_case("patch", {"contains": ["ok"]}, allowed_paths=["README.md"])
        parsed = {"case_id": "case-001", "files": [{"path": "secrets.txt", "content": "ok"}]}

        scored = module.score_case(parsed, case)

        self.assertIs(scored["schema_valid"], False)
        self.assertIs(scored["case_pass"], False)


if __name__ == "__main__":
    unittest.main()
