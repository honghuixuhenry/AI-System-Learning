import torch
import torch.nn as nn


class Model(nn.Module):

    def __init__(self):

        super().__init__()

        self.backbone = nn.Linear(
            128,
            128
        )

        self.head = nn.Linear(
            128,
            10
        )

    def forward(self, x):

        x = self.backbone(x)

        return self.head(x)


model = Model()


for parameter in model.backbone.parameters():

    parameter.requires_grad = False


for name, parameter in model.named_parameters():

    print(
        name,
        parameter.requires_grad
    )