scenarios = {
    "local_mac": {
        "hardware":
            "Apple Silicon",
        "priority":
            "local inference",
        "candidate_runtime":
            "llama.cpp"
    },

    "gpu_server": {
        "hardware":
            "NVIDIA GPU",
        "priority":
            "high concurrency",
        "candidate_runtime":
            "vLLM / SGLang"
    },

    "nvidia_optimized": {
        "hardware":
            "NVIDIA GPU",
        "priority":
            "hardware optimized inference",
        "candidate_runtime":
            "TensorRT-LLM"
    }
}


for name, config in (
    scenarios.items()
):
    print(name)

    for key, value in (
        config.items()
    ):
        print(
            " ",
            key,
            ":",
            value
        )