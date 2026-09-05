import torch
import torch.nn as nn
import torch.nn.functional as F


B = 2
T = 8
D = 32
D_FF = 96


x = torch.randn(
    B,
    T,
    D
)


gate_proj = nn.Linear(
    D,
    D_FF,
    bias=False
)


up_proj = nn.Linear(
    D,
    D_FF,
    bias=False
)


down_proj = nn.Linear(
    D_FF,
    D,
    bias=False
)


gate = gate_proj(
    x
)


up = up_proj(
    x
)


hidden = (
    F.silu(
        gate
    )
    *
    up
)


output = down_proj(
    hidden
)


print(
    "x:",
    x.shape
)

print(
    "gate:",
    gate.shape
)

print(
    "up:",
    up.shape
)

print(
    "hidden:",
    hidden.shape
)

print(
    "output:",
    output.shape
)