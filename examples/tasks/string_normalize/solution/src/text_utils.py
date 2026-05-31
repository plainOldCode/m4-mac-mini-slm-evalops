import re


def normalize_key(text: str) -> str:
    """Return a stable snake_case key for a user-facing label."""
    lowered = text.strip().lower()
    normalized = re.sub(r"[^a-z0-9]+", "_", lowered)
    return normalized.strip("_")
