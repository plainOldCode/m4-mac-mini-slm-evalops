import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.text_utils import normalize_key


class NormalizeKeyTests(unittest.TestCase):
    def test_lowercases_and_trims(self):
        self.assertEqual(normalize_key("  Samsung Electronics  "), "samsung_electronics")

    def test_replaces_punctuation_runs(self):
        self.assertEqual(normalize_key("HBM4E / Server-DRAM"), "hbm4e_server_dram")

    def test_handles_empty_punctuation(self):
        self.assertEqual(normalize_key(" - / "), "")


if __name__ == "__main__":
    unittest.main()
