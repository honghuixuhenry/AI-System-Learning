import torch
import torch.nn.functional as F


def attention(q, k, v):

    d = q.size(-1)

    scores = (
        q @ k.transpose(-2, -1)
    ) / (d ** 0.5)

    weights = F.softmax(
        scores,
        dim=-1
    )

    return weights @ v