engines = [
    {
        "name": "engine_A",
        "ttft_ms": 180,
        "output_tps": 1500,
        "gpu_memory_gib": 30
    },
    {
        "name": "engine_B",
        "ttft_ms": 220,
        "output_tps": 1800,
        "gpu_memory_gib": 27
    }
]


for engine in engines:

    print(
        engine["name"]
    )

    print(
        "TTFT:",
        engine["ttft_ms"]
    )

    print(
        "Throughput:",
        engine["output_tps"]
    )

    print(
        "Memory:",
        engine["gpu_memory_gib"]
    )

    print()