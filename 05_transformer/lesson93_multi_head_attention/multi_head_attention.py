import math

import torch
import torch.nn as nn


class MultiHeadSelfAttention(
    nn.Module
):

    def __init__(
        self,
        dim,
        num_heads
    ):

        super().__init__()


        assert (
            dim % num_heads == 0
        )


        self.dim = dim
        self.num_heads = num_heads
        self.head_dim = (
            dim // num_heads
        )


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


        self.out_proj = nn.Linear(
            dim,
            dim,
            bias=False
        )


    def forward(
        self,
        x
    ):

        B, T, D = x.shape


        Q = self.q_proj(x)
        K = self.k_proj(x)
        V = self.v_proj(x)


        Q = Q.reshape(
            B,
            T,
            self.num_heads,
            self.head_dim
        ).transpose(
            1,
            2
        )

        K = K.reshape(
            B,
            T,
            self.num_heads,
            self.head_dim
        ).transpose(
            1,
            2
        )

        V = V.reshape(
            B,
            T,
            self.num_heads,
            self.head_dim
        ).transpose(
            1,
            2
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
                self.head_dim
            )
        )


        weights = torch.softmax(
            scores,
            dim=-1
        )


        context = (
            weights
            @
            V
        )


        context = (
            context
            .transpose(
                1,
                2
            )
            .reshape(
                B,
                T,
                D
            )
        )


        output = self.out_proj(
            context
        )


        return (
            output,
            weights
        )