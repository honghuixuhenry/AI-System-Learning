import torch
import torch.nn.functional as F


gate = torch.tensor([
    -2.0,
    0.0,
    2.0
])


value = torch.tensor([
    10.0,
    10.0,
    10.0
])


activated_gate = F.silu(
    gate
)


output = (
    activated_gate
    *
    value
)


print(
    "gate:",
    gate
)

print(
    "activated gate:",
    activated_gate
)

print(
    "value:",
    value
)

print(
    "output:",
    output
)