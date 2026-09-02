import torch
import torch.nn as nn


x = torch.tensor([
    [1.0, 2.0, 3.0, 4.0],
    [10.0, 20.0, 30.0, 40.0]
])


ln = nn.LayerNorm(
    normalized_shape=4
)


y = ln(x)


print(
    "input:"
)

print(x)

print(
    "output:"
)

print(y)