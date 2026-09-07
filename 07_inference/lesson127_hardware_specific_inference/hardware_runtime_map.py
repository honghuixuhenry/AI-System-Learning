hardware_runtime_map = {
    "nvidia_datacenter_gpu": [
        "vLLM",
        "SGLang",
        "TensorRT-LLM"
    ],

    "apple_silicon": [
        "llama.cpp"
    ],

    "cpu": [
        "llama.cpp"
    ],

    "nvidia_edge": [
        "TensorRT-based runtime",
        "CUDA-optimized runtime"
    ]
}


for hardware, runtimes in (
    hardware_runtime_map.items()
):
    print(
        hardware,
        "->",
        runtimes
    )