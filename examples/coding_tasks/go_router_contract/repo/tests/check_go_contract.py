import re
from pathlib import Path

source = (Path(__file__).resolve().parents[1] / "src" / "router.go").read_text()

assert re.search(r"package\s+portfolio", source), "package must remain portfolio"
assert re.search(r"type\s+RouteDecision\s+struct\s*{", source), "RouteDecision struct is required"
assert re.search(r"Account\s+string", source), "RouteDecision.Account string field is required"
assert re.search(r"Reason\s+string", source), "RouteDecision.Reason string field is required"
assert re.search(r"func\s+RouteForSymbol\s*\(\s*symbol\s+string\s*\)\s+RouteDecision", source), "RouteForSymbol must return RouteDecision"
assert "005930" in source and "SEC" in source and '"C"' in source, "Samsung/SEC route to account C is required"
assert "000660" in source and "SKH" in source and '"D"' in source, "SKH route to account D is required"
assert '"WATCH"' in source, "Unknown symbols must route to WATCH"
assert re.search(r"strings\.(HasPrefix|ToUpper)", source) or "hasPrefix" in source, "Use prefix/case handling"
assert "no account" in source.lower() or "unknown" in source.lower(), "WATCH reason should explain no match"

print("go route contract checks passed")
