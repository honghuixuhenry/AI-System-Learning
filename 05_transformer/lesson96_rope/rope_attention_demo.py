import math

import torch
import torch.nn as nn


B = 2
T = 5
D = 16
H = 4

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


cos, sin = build_rope_cache(
    T,
    head_dim,
    x.device
)


Q = apply_rope(
    Q,
    cos,
    sin
)

K = apply_rope(
    K,
    cos,
    sin
)


scores = (
    Q
    @
    K.transpose(
        -2,
        -1
    )
)


scores = (
    scores
    /
    math.sqrt(
        head_dim
    )
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

print(
    "scores:",
    scores.shape
)