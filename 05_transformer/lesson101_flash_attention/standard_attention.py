import math

import torch


def standard_attention(
    q,
    k,
    v,
    causal=False
):
    # q/k/v:
    # (B,H,T,Dh)

    scores = (
        q
        @
        k.transpose(
            -2,
            -1
        )
    )

    scores = (
        scores
        /
        math.sqrt(
            q.shape[-1]
        )
    )

    if causal:

        T = q.shape[-2]

        mask = torch.tril(
            torch.ones(
                T,
                T,
                dtype=torch.bool,
                device=q.device
            )
        )

        scores = scores.masked_fill(
            ~mask,
            float("-inf")
        )

    weights = torch.softmax(
        scores,
        dim=-1
    )

    output = (
        weights
        @
        v
    )

    return output