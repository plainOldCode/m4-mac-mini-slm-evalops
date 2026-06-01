def parse_allocations(lines):
    rows = []
    for line in lines:
        text = line.strip()
        if not text or text.startswith("#"):
            continue
        symbol, raw_weight = text.split(":")
        weight = float(raw_weight.strip().rstrip("%")
        rows.append({"symbol": symbol.strip().upper(), "weight_pct": weight})
    return rows
