def parse_allocations(lines):
    rows = []
    for line in lines:
        text = line.strip()
        if not text or text.startswith("#"):
            continue
        if ":" not in text:
            raise ValueError(f"malformed allocation line: {line}")
        symbol, raw_weight = text.split(":", 1)
        symbol = symbol.strip().upper()
        if not symbol:
            raise ValueError(f"missing symbol: {line}")
        try:
            weight = float(raw_weight.strip().rstrip("%"))
        except ValueError as exc:
            raise ValueError(f"invalid weight: {line}") from exc
        if weight < 0:
            raise ValueError(f"negative weight: {line}")
        rows.append({"symbol": symbol, "weight_pct": weight})
    return sorted(rows, key=lambda item: item["symbol"])
