import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.allocation import parse_allocations


class AllocationParserTests(unittest.TestCase):
    def test_parse_and_sort(self):
        self.assertEqual(
            parse_allocations([" SKH: 54.5% ", "SEC:45.5"]),
            [
                {"symbol": "SEC", "weight_pct": 45.5},
                {"symbol": "SKH", "weight_pct": 54.5},
            ],
        )

    def test_ignore_blank_and_comments(self):
        self.assertEqual(parse_allocations(["", "# target", "cash:0"]), [{"symbol": "CASH", "weight_pct": 0.0}])

    def test_reject_malformed(self):
        with self.assertRaises(ValueError):
            parse_allocations(["SEC 45"])

    def test_reject_negative(self):
        with self.assertRaises(ValueError):
            parse_allocations(["SKH:-1"])


if __name__ == "__main__":
    unittest.main()
