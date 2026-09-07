import torch
import torch.nn as nn


class TinyModel(nn.Module):

    def __init__(self):

        super().__init__()

        self.linear1 = nn.Linear(
            128,
            256
        )

        self.linear2 = nn.Linear(
            256,
            128
        )

    def forward(self, x):

        x = self.linear1(x)

        x = torch.relu(x)

        return self.linear2(x)


model = TinyModel()


for parameter in model.parameters():

    parameter.requires_grad = True


trainable_parameters = sum(
    p.numel()
    for p in model.parameters()
    if p.requires_grad
)


total_parameters = sum(
    p.numel()
    for p in model.parameters()
)


print(
    "Total parameters:",
    total_parameters
)

print(
    "Trainable parameters:",
    trainable_parameters
)