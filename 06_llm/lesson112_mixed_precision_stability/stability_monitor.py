import torch


def check_loss(
    loss
):

    if not torch.isfinite(
        loss
    ):

        raise RuntimeError(
            "Non-finite loss detected"
        )