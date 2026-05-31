import re


def normalize_key(text: str) -> str:
    """Normalize a label into lowercase snake_case."""
    key = re.sub(r"[^a-z0-9]+", "_", text.strip().lower())
    return key.strip("_")
