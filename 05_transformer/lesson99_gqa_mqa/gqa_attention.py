import math

import torch
import torch.nn as nn


class GroupedQueryAttention(
    nn.Module
):

    def __init__(
        self,
        dim,
        num_q_heads,
        num_kv_heads
    ):

        super().__init__()


        assert (
            dim
            %
            num_q_heads
            ==
            0
        )


        assert (
            num_q_heads
            %
            num_kv_heads
            ==
            0
        )


        self.dim = dim

        self.num_q_heads = (
            num_q_heads
        )

        self.num_kv_heads = (
            num_kv_heads
        )


        self.head_dim = (
            dim
            //
            num_q_heads
        )


        self.group_size = (
            num_q_heads
            //
            num_kv_heads
        )


        self.q_proj = nn.Linear(
            dim,
            num_q_heads
            *
            self.head_dim,
            bias=False
        )


        self.k_proj = nn.Linear(
            dim,
            num_kv_heads
            *
            self.head_dim,
            bias=False
        )


        self.v_proj = nn.Linear(
            dim,
            num_kv_heads
            *
            self.head_dim,
            bias=False
        )


        self.out_proj = nn.Linear(
            dim,
            dim,
            bias=False
        )

    