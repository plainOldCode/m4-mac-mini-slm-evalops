def normalize_key(text: str) -> str:
    """Return a stable key for a user-facing label."""
    return text.strip()
