import re


def normalize_key(text: str) -> str:
    """Return a stable key for a user-facing label."""
    cleaned = re.sub(r"[^0-9A-Za-z]+", "_", text.strip().lower())
    return cleaned.strip("_")
