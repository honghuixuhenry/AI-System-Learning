import torch
import torch.nn as nn


B = 1
T = 3
D = 4


x = torch.randn(
    B,
    T,
    D
)


q_proj = nn.Linear(
    D,
    D,
    bias=False
)

k_proj = nn.Linear(
    D,
    D,
    bias=False
)


Q = q_proj(x)
K = k_proj(x)


scores = (
    Q
    @
    K.transpose(
        -2,
        -1
    )
)


print(
    scores
)

print(
    scores.shape
)