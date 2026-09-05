import torch


def rotate_pairs(
    x,
    cos,
    sin
):

    x_even = x[..., 0::2]
    x_odd = x[..., 1::2]


    out_even = (
        x_even * cos
        -
        x_odd * sin
    )


    out_odd = (
        x_even * sin
        +
        x_odd * cos
    )


    output = torch.empty_like(
        x
    )


    output[..., 0::2] = (
        out_even
    )

    output[..., 1::2] = (
        out_odd
    )


    return output