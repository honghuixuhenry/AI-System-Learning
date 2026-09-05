import math

import torch
import torch.nn as nn
import torch.nn.functional as F


class CausalGQAAttention(nn.Module):

    def __init__(
        self,
        config
    ):

        super().__init__()

        self.dim = config.dim

        self.num_q_heads = (
            config.num_q_heads
        )

        self.num_kv_heads = (
            config.num_kv_heads
        )

        assert (
            self.dim
            %
            self.num_q_heads
            ==
            0
        )

        assert (
            self.num_q_heads
            %
            self.num_kv_heads
            ==
            0
        )

        self.head_dim = (
            self.dim
            //
            self.num_q_heads
        )

        self.group_size = (
            self.num_q_heads
            //
            self.num_kv_heads
        )

        self.q_proj = nn.Linear(
            self.dim,
            self.num_q_heads
            *
            self.head_dim,
            bias=False
        )

        self.k_proj = nn.Linear(
            self.dim,
            self.num_kv_heads
            *
            self.head_dim,
            bias=False
        )

        self.v_proj = nn.Linear(
            self.dim,
            self.num_kv_heads
            *
            self.head_dim,
            bias=False
        )

        self.out_proj = nn.Linear(
            self.dim,
            self.dim,
            bias=False
        )