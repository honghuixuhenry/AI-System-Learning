import torch.nn as nn


class LayerNormClassifier(
    nn.Module
):

    def __init__(
        self
    ):
        super().__init__()

        self.network = nn.Sequential(

            nn.Linear(
                20,
                64
            ),

            nn.LayerNorm(
                64
            ),

            nn.ReLU(),

            nn.Linear(
                64,
                64
            ),

            nn.LayerNorm(
                64
            ),

            nn.ReLU(),

            nn.Linear(
                64,
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