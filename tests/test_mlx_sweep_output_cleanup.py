from __future__ import annotations

import importlib.util
import sys
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "run_mlx_candidate_sweep.py"
spec = importlib.util.spec_from_file_location("run_mlx_candidate_sweep", SCRIPT)
assert spec is not None
module = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules[spec.name] = module
spec.loader.exec_module(module)


def test_empty_think_wrapper_promotes_schema_valid_json() -> None:
    output = """<think>
</think>

{"summary": "요약", "sentiment": "bullish", "companies": ["삼성전자"]}
"""

    parsed = module.analyze_output(output)

    assert parsed["think_leak"] is True
    assert parsed["output_cleanup_applied"] is True
    assert parsed["output_cleanup_reason"] == "empty_think_wrapper_removed"
    assert parsed["json_valid"] is True
    assert parsed["schema_valid"] is True
    assert module.recommend("ok", parsed) == "candidate_for_core_tasks_after_cleanup"


def test_nonempty_think_without_json_stays_reasoning_lane() -> None:
    output = """<think>
I should reason about the answer first.
</think>
The answer is bullish because Samsung is improving.
"""

    parsed = module.analyze_output(output)

    assert parsed["think_leak"] is True
    assert parsed["output_cleanup_applied"] is True
    assert parsed["output_cleanup_reason"] == "think_block_removed"
    assert parsed["json_valid"] is False
    assert parsed["schema_valid"] is False
    assert module.recommend("ok", parsed) == "reasoning_lane_protocol_mismatch"
