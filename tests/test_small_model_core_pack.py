from __future__ import annotations

import json
import unittest
from pathlib import Path


PACK_DIR = Path(__file__).resolve().parents[1] / "benchmark_packs" / "small-model-core"


class SmallModelCorePackTest(unittest.TestCase):
    def test_pack_has_expected_lanes_and_weights(self) -> None:
        pack = json.loads((PACK_DIR / "pack.json").read_text())

        lanes = {lane["id"]: lane for lane in pack["lanes"]}

        self.assertEqual(set(lanes), {"summary", "extraction", "protocol", "patch"})
        self.assertEqual(sum(lane["weight"] for lane in lanes.values()), 1.0)
        self.assertTrue(all(lane["cases"] for lane in lanes.values()))

    def test_case_ids_are_unique(self) -> None:
        pack = json.loads((PACK_DIR / "pack.json").read_text())
        case_ids = [
            case["case_id"]
            for lane in pack["lanes"]
            for case in lane["cases"]
        ]

        self.assertEqual(len(case_ids), len(set(case_ids)))

    def test_patch_cases_have_existing_fixtures_and_allowed_paths(self) -> None:
        pack = json.loads((PACK_DIR / "pack.json").read_text())
        patch_lane = next(lane for lane in pack["lanes"] if lane["id"] == "patch")

        for case in patch_lane["cases"]:
            fixture_dir = PACK_DIR / case["fixture_dir"]
            solution_dir = PACK_DIR / case["solution_dir"]

            self.assertTrue(fixture_dir.exists())
            self.assertTrue(solution_dir.exists())
            self.assertTrue(case["allowed_paths"])
            for relative_path in case["allowed_paths"]:
                self.assertTrue((fixture_dir / relative_path).exists())
                self.assertTrue((solution_dir / relative_path).exists())

    def test_protocol_cases_require_json_only(self) -> None:
        pack = json.loads((PACK_DIR / "pack.json").read_text())
        protocol_lane = next(lane for lane in pack["lanes"] if lane["id"] == "protocol")

        for case in protocol_lane["cases"]:
            self.assertIn("Return JSON only", case["prompt"])
            self.assertIn("expected", case)


if __name__ == "__main__":
    unittest.main()
