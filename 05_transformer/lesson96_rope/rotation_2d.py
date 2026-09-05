import math

import torch


x = torch.tensor([
    1.0,
    0.0
])


theta = math.pi / 2


rotation = torch.tensor([
    [
        math.cos(theta),
        -math.sin(theta)
    ],
    [
        math.sin(theta),
        math.cos(theta)
    ]
])


rotated = rotation @ x


print(
    "original:",
    x
)

print(
    "rotated:",
    rotated
)