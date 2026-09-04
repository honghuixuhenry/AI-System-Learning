import torch
import torch.nn as nn


class PreNormResidualBlock(nn.Module):

    def __init__(self, dim):

        super().__init__()

        self.norm = nn.LayerNorm(
            dim
        )

        self.net = nn.Sequential(
            nn.Linear(dim, dim),
            nn.ReLU(),
            nn.Linear(dim, dim)
        )


    def forward(self, x):

        return x + self.net(
            self.norm(x)
        )