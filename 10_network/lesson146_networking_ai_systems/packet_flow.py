def split_payload(
    payload_size: int,
    segment_size: int
):

    segments = []

    remaining = payload_size

    while remaining > 0:

        size = min(
            segment_size,
            remaining
        )

        segments.append(size)

        remaining -= size

    return segments