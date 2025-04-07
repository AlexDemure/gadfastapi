def to_clean(string: str | None) -> str | None:
    return string.strip() if string else None


def to_lower(string: str | None) -> str | None:
    return to_clean(string).lower() if string else None
