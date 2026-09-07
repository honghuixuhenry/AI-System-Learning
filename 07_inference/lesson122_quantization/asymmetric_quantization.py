import torch


def quantize_asymmetric(
    tensor,
    num_bits=8
):

    qmin = 0

    qmax = (
        2 ** num_bits
        -
        1
    )


    x_min = tensor.min()

    x_max = tensor.max()


    scale = (
        (x_max - x_min)
        /
        (qmax - qmin)
    )


    zero_point = (
        qmin
        -
        x_min / scale
    )


    zero_point = torch.round(
        zero_point
    )


    q = torch.round(
        tensor / scale
        +
        zero_point
    )


    q = torch.clamp(
        q,
        qmin,
        qmax
    )


    return (
        q,
        scale,
        zero_point
    )