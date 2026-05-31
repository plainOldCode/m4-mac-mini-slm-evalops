from __future__ import annotations

import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "run_openclaw_tool_adapter_suite.py"
spec = importlib.util.spec_from_file_location("run_openclaw_tool_adapter_suite", SCRIPT)
assert spec is not None
module = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules[spec.name] = module
spec.loader.exec_module(module)


class OpenClawToolAdapterSuiteTest(unittest.TestCase):
    def test_extracts_safe_intent_from_response_path(self) -> None:
        token = "native_tool_ok_fa29878048a4"
        path = Path(tempfile.gettempdir()) / f"openclaw-native-tool-{token}.txt"
        response = f"{token} written to {path}"

        intent = module.extract_adapter_intent(response_text=response)

        self.assertIsNotNone(intent)
        assert intent is not None
        self.assertEqual(intent.token, token)
        self.assertEqual(intent.path, str(path))
        self.assertEqual(intent.source, "response")

    def test_extracts_safe_intent_from_prompt_trace_path(self) -> None:
        token = "native_tool_ok_3107f8757c4c"
        path = Path(tempfile.gettempdir()) / f"openclaw-native-tool-{token}.txt"
        response = f"**{token}**"
        trace = f"finalPromptText: printf {token} > {path}"

        intent = module.extract_adapter_intent(response_text=response, error_tail=trace)

        self.assertIsNotNone(intent)
        assert intent is not None
        self.assertEqual(intent.token, token)
        self.assertEqual(intent.path, str(path))
        self.assertEqual(intent.source, "prompt-trace")

    def test_rejects_non_temp_path(self) -> None:
        token = "native_tool_ok_fa29878048a4"
        response = f"{token} written to /Users/miniadmin/openclaw-native-tool-{token}.txt"

        self.assertIsNone(module.extract_adapter_intent(response_text=response))

    def test_rejects_mismatched_token_and_path(self) -> None:
        token = "native_tool_ok_fa29878048a4"
        other = "native_tool_ok_3107f8757c4c"
        path = Path(tempfile.gettempdir()) / f"openclaw-native-tool-{other}.txt"
        response = f"{token} written to {path}"

        self.assertIsNone(module.extract_adapter_intent(response_text=response))


if __name__ == "__main__":
    unittest.main()
