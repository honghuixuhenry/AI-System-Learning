import torch.nn as nn


class Classifier(
    nn.Module
):

    def __init__(
        self
    ):

        super().__init__()

        self.network = nn.Sequential(

            nn.Linear(
                2,
                16
            ),

            nn.ReLU(),

            nn.Linear(
                16,
                16
            ),

            nn.ReLU(),

            nn.Linear(
                16,
                3
            )
        )

    def forward(
        self,
        x
    ):

        return self.network(
            x
        )