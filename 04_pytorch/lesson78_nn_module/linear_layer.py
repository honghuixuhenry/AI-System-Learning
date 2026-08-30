import torch
import torch.nn as nn


layer = nn.Linear(
    3,
    2
)


x = torch.tensor(
    [
        [1.0, 2.0, 3.0]
    ]
)


y = layer(x)


print(
    "input shape:",
    x.shape
)

print(
    "output shape:",
    y.shape
)

print(y)