import math

import torch
import torch.nn as nn


class SelfAttention(nn.Module):

    def __init__(
        self,
        dim
    ):

        super().__init__()


        self.dim = dim


        self.q_proj = nn.Linear(
            dim,
            dim,
            bias=False
        )

        self.k_proj = nn.Linear(
            dim,
            dim,
            bias=False
        )

        self.v_proj = nn.Linear(
            dim,
            dim,
            bias=False
        )


    def forward(
        self,
        x
    ):

        Q = self.q_proj(
            x
        )

        K = self.k_proj(
            x
        )

        V = self.v_proj(
            x
        )


        scores = (
            Q
            @
            K.transpose(
                -2,
                -1
            )
        )


        scores = (
            scores
            /
            math.sqrt(
                self.dim
            )
        )


        weights = torch.softmax(
            scores,
            dim=-1
        )


        output = (
            weights
            @
            V
        )


        return output