def chunk_text(
    text,
    chunk_size=20
):
    words = text.split()

    chunks = []

    for start in range(
        0,
        len(words),
        chunk_size
    ):
        chunk = words[
            start:
            start + chunk_size
        ]

        chunks.append(
            " ".join(chunk)
        )

    return chunks