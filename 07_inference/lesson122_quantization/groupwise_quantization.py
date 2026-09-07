import torch


def quantize_groupwise(
    tensor,
    group_size=4,
    num_bits=8
):

    flat = tensor.flatten()

    qmax = (
        2 ** (num_bits - 1)
        -
        1
    )


    quantized_groups = []

    scales = []


    for start in range(
        0,
        flat.numel(),
        group_size
    ):

        group = flat[
            start:
            start + group_size
        ]


        max_abs = (
            group.abs().max()
        )


        scale = (
            max_abs / qmax
        )


        q = torch.round(
            group / scale
        )


        q = torch.clamp(
            q,
            -qmax,
            qmax
        )


        quantized_groups.append(
            q
        )

        scales.append(
            scale
        )


    return (
        torch.cat(
            quantized_groups
        ),
        scales
    )