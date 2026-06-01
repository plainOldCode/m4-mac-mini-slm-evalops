import re
from pathlib import Path

source = (Path(__file__).resolve().parents[1] / "src" / "lib.rs").read_text()

assert re.search(r"pub\s+struct\s+Holding\s*{", source), "public Holding struct is required"
assert re.search(r"symbol\s*:\s*String", source), "Holding.symbol String field is required"
assert re.search(r"quantity\s*:\s*u32", source), "Holding.quantity u32 field is required"
assert re.search(r"pub\s+fn\s+parse_holding\s*\(\s*input\s*:\s*&str\s*\)\s*->\s*Result\s*<\s*Holding\s*,\s*String\s*>", source), "parse_holding must return Result<Holding, String>"
assert ".split_once" in source or ".splitn" in source, "Use explicit colon splitting"
assert ".trim()" in source, "Trim input parts"
assert ".to_uppercase()" in source, "Uppercase the symbol"
assert ".parse::<u32>()" in source or ".parse()" in source, "Parse quantity as an integer"
assert ".unwrap()" not in source and ".expect(" not in source, "Do not use unwrap or expect"
assert "Err(" in source and "Ok(" in source, "Return both Ok and Err branches"

print("rust result contract checks passed")
