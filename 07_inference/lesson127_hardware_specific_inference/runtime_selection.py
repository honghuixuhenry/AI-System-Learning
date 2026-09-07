def recommend_runtime(
    hardware,
    workload
):

    if hardware == "nvidia_gpu":

        if workload == "large_scale_server":
            return [
                "vLLM",
                "SGLang",
                "TensorRT-LLM"
            ]

        return [
            "vLLM",
            "TensorRT-LLM"
        ]

    if hardware == "apple_silicon":
        return [
            "llama.cpp"
        ]

    if hardware == "cpu":
        return [
            "llama.cpp"
        ]

    return [
        "benchmark available runtimes"
    ]