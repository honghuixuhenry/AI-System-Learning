SUSPICIOUS_PATTERNS = [
    "ignore previous",
    "ignore the system",
    "override instructions",
    "reveal hidden",
    "change your task"
]


def detect_suspicious_text(
    text: str
) -> bool:

    lowered = text.lower()

    return any(
        pattern in lowered
        for pattern in SUSPICIOUS_PATTERNS
    )