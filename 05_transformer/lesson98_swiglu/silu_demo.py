import torch
import torch.nn.functional as F


x = torch.tensor([
    -3.0,
    -1.0,
    0.0,
    1.0,
    3.0
])


sigmoid = torch.sigmoid(
    x
)


manual_silu = (
    x * sigmoid
)


pytorch_silu = F.silu(
    x
)


print(
    "x:",
    x
)

print(
    "sigmoid:",
    sigmoid
)

print(
    "manual SiLU:",
    manual_silu
)

print(
    "PyTorch SiLU:",
    pytorch_silu
)