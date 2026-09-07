import torch


def quantize_symmetric(
    tensor,
    num_bits=8
):

    qmax = (
        2 ** (num_bits - 1)
        -
        1
    )

    max_abs = (
        tensor.abs().max()
    )

    scale = (
        max_abs / qmax
    )

    q = torch.round(
        tensor / scale
    )

    q = torch.clamp(
        q,
        -qmax,
        qmax
    )

    return (
        q,
        scale
    )


def dequantize(
    q,
    scale
):

    return (
        q * scale
    )


x = torch.tensor([
    -2.0,
    -1.0,
    0.0,
    1.0,
    2.0
])


q, scale = quantize_symmetric(
    x
)


x_hat = dequantize(
    q,
    scale
)


print("Original:", x)

print("Quantized:", q)

print("Recovered:", x_hat)