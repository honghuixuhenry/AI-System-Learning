import torch
import torch.nn as nn


model = nn.Sequential(

    nn.Linear(
        10,
        20
    ),

    nn.Linear(
        20,
        5
    )
)


total_parameters = sum(
    p.numel()
    for p in model.parameters()
)


trainable_parameters = sum(
    p.numel()
    for p in model.parameters()
    if p.requires_grad
)


print(
    "total:",
    total_parameters
)

print(
    "trainable:",
    trainable_parameters
)