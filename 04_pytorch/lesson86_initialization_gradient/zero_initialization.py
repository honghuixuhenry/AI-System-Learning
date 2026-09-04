import torch
import torch.nn as nn


layer = nn.Linear(
    3,
    4
)


nn.init.zeros_(
    layer.weight
)

nn.init.zeros_(
    layer.bias
)


print(
    layer.weight
)