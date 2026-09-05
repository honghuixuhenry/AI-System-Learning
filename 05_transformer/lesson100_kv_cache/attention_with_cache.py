import math

import torch
import torch.nn as nn


class CachedCausalAttention(
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
        x,
        past_k=None,
        past_v=None
    ):

        B, T_new, D = x.shape


        q = self.q_proj(
            x
        )

        k_new = self.k_proj(
            x
        )

        v_new = self.v_proj(
            x
        )


        q = q.reshape(
            B,
            T_new,
            self.num_heads,
            self.head_dim
        ).transpose(
            1,
            2
        )


        k_new = k_new.reshape(
            B,
            T_new,
            self.num_heads,
            self.head_dim
        ).transpose(
            1,
            2
        )


        v_new = v_new.reshape(
            B,
            T_new,
            self.num_heads,
            self.head_dim
        ).transpose(
            1,
            2
        )


        if past_k is None:

            k = k_new
            v = v_new

        else:

            k = torch.cat(
                [
                    past_k,
                    k_new
                ],
                dim=2
            )

            v = torch.cat(
                [
                    past_v,
                    v_new
                ],
                dim=2
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
                T_new,
                D
            )
        )


        output = self.out_proj(
            context
        )


        return (
            output,
            k,
            v
        )