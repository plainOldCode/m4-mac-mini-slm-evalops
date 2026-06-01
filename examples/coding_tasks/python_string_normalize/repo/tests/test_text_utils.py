import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.text_utils import normalize_key


class NormalizeKeyTests(unittest.TestCase):
    def test_lowercase_and_trim(self):
        self.assertEqual(normalize_key("  Samsung Electronics  "), "samsung_electronics")

    def test_collapse_separator_runs(self):
        self.assertEqual(normalize_key("HBM4E / Server-DRAM"), "hbm4e_server_dram")

    def test_empty_after_cleanup(self):
        self.assertEqual(normalize_key(" - / "), "")

    def test_preserves_digits(self):
        self.assertEqual(normalize_key("Qwen3 4B Instruct"), "qwen3_4b_instruct")


if __name__ == "__main__":
    unittest.main()
