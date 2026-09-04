import torch
import torch.nn as nn


class DeepSigmoidNet(
    nn.Module
):

    def __init__(
        self
    ):
        super().__init__()

        layers = []

        for _ in range(
            20
        ):
            layers.append(
                nn.Linear(
                    32,
                    32
                )
            )

            layers.append(
                nn.Sigmoid()
            )

        self.network = nn.Sequential(
            *layers
        )

    def forward(
        self,
        x
    ):
        return self.network(
            x
        )

model = DeepSigmoidNet()

x = torch.randn(
    16,
    32
)

target = torch.randn(
    16,
    32
)


output = model(x)

loss = nn.MSELoss()(
    output,
    target
)

loss.backward()

for name, param in model.named_parameters():

    if param.grad is not None:

        print(
            name,
            param.grad.norm().item()
        )