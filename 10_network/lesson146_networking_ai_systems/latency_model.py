def transfer_time_seconds(
    size_bytes: int,
    bandwidth_bps: float
) -> float:

    size_bits = (
        size_bytes * 8
    )

    return (
        size_bits
        /
        bandwidth_bps
    )


def total_request_latency(
    network_latency: float,
    queue_latency: float,
    compute_latency: float
) -> float:

    return (
        network_latency
        +
        queue_latency
        +
        compute_latency
    )