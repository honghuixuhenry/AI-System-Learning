import torch
import torch.nn as nn


B = 2
T = 4
D = 8


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

v_proj = nn.Linear(
    D,
    D,
    bias=False
)


Q = q_proj(x)
K = k_proj(x)
V = v_proj(x)


print(
    "X:",
    x.shape
)

print(
    "Q:",
    Q.shape
)

print(
    "K:",
    K.shape
)

print(
    "V:",
    V.shape
)