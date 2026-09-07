import torch
import torch.nn as nn


stage0 = nn.Sequential(
    nn.Linear(8, 8),
    nn.ReLU(),
    nn.Linear(8, 8)
)


stage1 = nn.Sequential(
    nn.Linear(8, 8),
    nn.ReLU(),
    nn.Linear(8, 8)
)


x = torch.randn(
    4,
    8
)


activation = stage0(
    x
)


output = stage1(
    activation
)


print(
    output.shape
)