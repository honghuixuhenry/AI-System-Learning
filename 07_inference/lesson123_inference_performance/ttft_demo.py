import time


def simulate_request(
    queue_time,
    prefill_time
):
    start = time.perf_counter()

    time.sleep(queue_time)
    time.sleep(prefill_time)

    first_token_time = (
        time.perf_counter()
    )

    ttft = (
        first_token_time
        -
        start
    )

    return ttft


ttft = simulate_request(
    queue_time=0.05,
    prefill_time=0.10
)

print(
    "TTFT:",
    ttft,
    "seconds"
)