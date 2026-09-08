from latency_model import (
    transfer_time_seconds,
    total_request_latency
)


prompt_size = (
    100 * 1024
)

bandwidth = (
    1_000_000_000
)


transfer_time = (
    transfer_time_seconds(
        prompt_size,
        bandwidth
    )
)


total = (
    total_request_latency(
        network_latency=0.010,
        queue_latency=0.020,
        compute_latency=0.150
    )
)


print(
    "Prompt transfer time:",
    transfer_time,
    "seconds"
)

print(
    "Total request latency:",
    total,
    "seconds"
)