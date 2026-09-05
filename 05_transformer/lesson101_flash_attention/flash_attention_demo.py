import math

import torch
import torch.nn.functional as F


def manual_attention(
    q,
    k,
    v
):
    T = q.shape[-2]

    scores = (
        q
        @
        k.transpose(
            -2,
            -1
        )
    ) / math.sqrt(
        q.shape[-1]
    )


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


    return (
        weights
        @
        v
    )


B = 2
H = 4
T = 64
D = 32


q = torch.randn(
    B,
    H,
    T,
    D
)

k = torch.randn_like(
    q
)

v = torch.randn_like(
    q
)


manual = manual_attention(
    q,
    k,
    v
)


sdpa = (
    F.scaled_dot_product_attention(
        q,
        k,
        v,
        is_causal=True
    )
)


print(
    "manual:",
    manual.shape
)

print(
    "SDPA:",
    sdpa.shape
)


print(
    torch.allclose(
        manual,
        sdpa,
        atol=1e-5,
        rtol=1e-4
    )
)