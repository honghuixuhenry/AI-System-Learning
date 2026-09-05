import torch


def online_softmax_stats(
    blocks
):
    m = torch.tensor(
        float("-inf")
    )

    l = torch.tensor(
        0.0
    )

    for block in blocks:

        block_max = block.max()

        new_m = torch.maximum(
            m,
            block_max
        )

        old_scale = torch.exp(
            m - new_m
        )

        block_exp_sum = torch.exp(
            block - new_m
        ).sum()

        l = (
            l * old_scale
            +
            block_exp_sum
        )

        m = new_m

    return m, l