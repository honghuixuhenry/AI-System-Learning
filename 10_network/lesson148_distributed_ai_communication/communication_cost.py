def communication_time(
    size_bytes: int,
    startup_seconds: float,
    bandwidth_bytes_per_second: float
) -> float:

    transfer_time = (
        size_bytes
        /
        bandwidth_bytes_per_second
    )

    return (
        startup_seconds
        +
        transfer_time
    )