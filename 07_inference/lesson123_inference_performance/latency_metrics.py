def estimate_latency(
    ttft_ms,
    output_tokens,
    itl_ms
):

    if output_tokens <= 0:
        return ttft_ms

    return (
        ttft_ms
        +
        max(
            output_tokens - 1,
            0
        )
        *
        itl_ms
    )


latency = estimate_latency(
    ttft_ms=300,
    output_tokens=100,
    itl_ms=30
)

print(
    latency,
    "ms"
)