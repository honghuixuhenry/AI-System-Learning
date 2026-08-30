import torch
import torch.nn as nn


class SimpleModel(
    nn.Module
):

    def __init__(
        self
    ):

        super().__init__()

        self.layer1 = nn.Linear(
            3,
            4
        )

        self.layer2 = nn.Linear(
            4,
            2
        )

    def forward(
        self,
        x
    ):

        x = self.layer1(x)

        x = self.layer2(x)

        return x


model = SimpleModel()


x = torch.rand(
    5,
    3
)


output = model(x)


print(
    "input:",
    x.shape
)

print(
    "output:",
    output.shape
)


for name, parameter in (
    model.named_parameters()
):

    print(
        name,
        parameter.shape
    )