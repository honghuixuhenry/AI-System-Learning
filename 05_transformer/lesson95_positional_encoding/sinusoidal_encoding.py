import math

import torch


def sinusoidal_encoding(
    max_len,
    dim
):

    pe = torch.zeros(
        max_len,
        dim
    )


    position = torch.arange(
        max_len
    ).unsqueeze(
        1
    )


    div_term = torch.exp(
        torch.arange(
            0,
            dim,
            2
        )
        *
        (
            -math.log(10000.0)
            /
            dim
        )
    )


    pe[
        :,
        0::2
    ] = torch.sin(
        position
        *
        div_term
    )


    pe[
        :,
        1::2
    ] = torch.cos(
        position
        *
        div_term
    )


    return pe