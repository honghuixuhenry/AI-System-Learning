import torch
import torch.nn as nn


class ResidualBlock(nn.Module):

    def __init__(self, dim):

        super().__init__()

        self.net = nn.Sequential(
            nn.Linear(dim, dim),
            nn.ReLU(),
            nn.Linear(dim, dim)
        )

        self.activation = nn.ReLU()


    def forward(self, x):

        out = self.net(x)

        out = x + out

        out = self.activation(out)

        return out