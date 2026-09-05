import torch


def rms_norm(
    x,
    eps=1e-6
):

    mean_square = (
        x
        .pow(2)
        .mean(
            dim=-1,
            keepdim=True
        )
    )


    rms = torch.sqrt(
        mean_square
        +
        eps
    )


    return (
        x / rms
    )