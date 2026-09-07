import torch


def quantize_weight(
    weight,
    qmax=127
):

    max_abs = (
        weight.abs().max()
    )

    scale = (
        max_abs / qmax
    )


    q_weight = torch.round(
        weight / scale
    )


    q_weight = torch.clamp(
        q_weight,
        -qmax,
        qmax
    )


    return (
        q_weight,
        scale
    )


def quantized_linear(
    x,
    q_weight,
    scale
):

    weight = (
        q_weight
        *
        scale
    )

    return (
        x @ weight
    )