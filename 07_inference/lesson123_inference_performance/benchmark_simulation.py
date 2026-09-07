import statistics


requests = [
    {
        "ttft_ms": 200,
        "latency_ms": 1800,
        "output_tokens": 60
    },
    {
        "ttft_ms": 250,
        "latency_ms": 2000,
        "output_tokens": 70
    },
    {
        "ttft_ms": 180,
        "latency_ms": 1600,
        "output_tokens": 50
    }
]


ttfts = [
    request["ttft_ms"]
    for request in requests
]


latencies = [
    request["latency_ms"]
    for request in requests
]


total_tokens = sum(
    request["output_tokens"]
    for request in requests
)


benchmark_duration = 2.5


print(
    "Average TTFT:",
    statistics.mean(ttfts)
)


print(
    "Average latency:",
    statistics.mean(latencies)
)


print(
    "Output throughput:",
    total_tokens
    /
    benchmark_duration
)