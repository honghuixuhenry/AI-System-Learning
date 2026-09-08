def normalize_text(
    text: str
) -> str:

    return (
        text
        .lower()
        .strip()
    )


def classify(
    text: str
) -> str:

    text = normalize_text(
        text
    )

    if "approved" in text:
        return "approved"

    return "unknown"