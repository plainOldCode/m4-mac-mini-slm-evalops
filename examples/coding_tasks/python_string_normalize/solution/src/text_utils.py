import re


def normalize_key(text: str) -> str:
    lowered = text.strip().lower()
    normalized = re.sub(r"[^a-z0-9]+", "_", lowered)
    return normalized.strip("_")
