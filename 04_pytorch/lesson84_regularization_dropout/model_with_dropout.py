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
                64
            ),

            nn.ReLU(),

            nn.Dropout(
                p=0.3
            ),

            nn.Linear(
                64,
                64
            ),

            nn.ReLU(),

            nn.Dropout(
                p=0.3
            ),

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