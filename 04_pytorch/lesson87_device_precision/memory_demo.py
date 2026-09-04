import torch


def tensor_memory_mb(
    tensor
):

    bytes_used = (
        tensor.numel()
        *
        tensor.element_size()
    )

    return (
        bytes_used
        /
        1024
        /
        1024
    )


x32 = torch.zeros(
    1000,
    1000,
    dtype=torch.float32
)


x16 = torch.zeros(
    1000,
    1000,
    dtype=torch.float16
)


xbf16 = torch.zeros(
    1000,
    1000,
    dtype=torch.bfloat16
)


print(
    "FP32:",
    tensor_memory_mb(
        x32
    ),
    "MB"
)


print(
    "FP16:",
    tensor_memory_mb(
        x16
    ),
    "MB"
)


print(
    "BF16:",
    tensor_memory_mb(
        xbf16
    ),
    "MB"
)