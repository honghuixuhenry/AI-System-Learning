import torch
import torch.nn as nn


B = 2
T = 5
D = 8
H = 2


head_dim = D // H


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


Q = Q.reshape(
    B,
    T,
    H,
    head_dim
).transpose(
    1,
    2
)

K = K.reshape(
    B,
    T,
    H,
    head_dim
).transpose(
    1,
    2
)

V = V.reshape(
    B,
    T,
    H,
    head_dim
).transpose(
    1,
    2
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