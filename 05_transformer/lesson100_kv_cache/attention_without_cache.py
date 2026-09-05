import math

import torch
import torch.nn as nn


class CausalAttention(
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


        q = self.q_proj(x)
        k = self.k_proj(x)
        v = self.v_proj(x)


        q = q.reshape(
            B,
            T,
            self.num_heads,
            self.head_dim
        ).transpose(
            1,
            2
        )


        k = k.reshape(
            B,
            T,
            self.num_heads,
            self.head_dim
        ).transpose(
            1,
            2
        )


        v = v.reshape(
            B,
            T,
            self.num_heads,
            self.head_dim
        ).transpose(
            1,
            2
        )


        scores = (
            q
            @
            k.transpose(
                -2,
                -1
            )
        ) / math.sqrt(
            self.head_dim
        )


        mask = torch.tril(
            torch.ones(
                T,
                T,
                dtype=torch.bool,
                device=x.device
            )
        )


        scores = scores.masked_fill(
            ~mask,
            float("-inf")
        )


        weights = torch.softmax(
            scores,
            dim=-1
        )


        context = (
            weights
            @
            v
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


        return self.out_proj(
            context
        )