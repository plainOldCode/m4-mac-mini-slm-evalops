from html.parser import HTMLParser
from pathlib import Path
import re
import unittest


class TextParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text = []
        self.has_card = False
        self.has_heading = False
        self.has_metric_list = False

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        if attrs_dict.get("data-testid") == "model-status-card":
            self.has_card = True
        if tag in {"h1", "h2", "h3"}:
            self.has_heading = True
        if tag in {"ul", "ol", "dl"}:
            self.has_metric_list = True

    def handle_data(self, data):
        self.text.append(data)


class StatusCardTests(unittest.TestCase):
    def setUp(self):
        self.html = Path("index.html").read_text()
        self.css = Path("styles.css").read_text()
        self.parser = TextParser()
        self.parser.feed(self.html)
        self.visible_text = " ".join(" ".join(self.parser.text).split())

    def test_card_structure(self):
        self.assertTrue(self.parser.has_card)
        self.assertTrue(self.parser.has_heading)
        self.assertTrue(self.parser.has_metric_list)

    def test_required_copy(self):
        for phrase in ["Qwen3 4B", "OpenClaw Native", "Pass", "90/100"]:
            self.assertIn(phrase, self.visible_text)

    def test_css_contract(self):
        self.assertIn(".status-card", self.css)
        self.assertRegex(self.css, r"display\s*:\s*(grid|flex)")
        self.assertIn("@media", self.css)
        matches = re.findall(r"border-radius\s*:\s*(\d+(?:\.\d+)?)px", self.css)
        self.assertTrue(matches)
        self.assertLessEqual(max(float(value) for value in matches), 8)


if __name__ == "__main__":
    unittest.main()
