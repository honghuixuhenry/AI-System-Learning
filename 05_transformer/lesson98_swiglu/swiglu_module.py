import torch
import torch.nn as nn
import torch.nn.functional as F


class SwiGLU(nn.Module):

    def __init__(
        self,
        dim,
        hidden_dim
    ):

        super().__init__()


        self.gate_proj = nn.Linear(
            dim,
            hidden_dim,
            bias=False
        )


        self.up_proj = nn.Linear(
            dim,
            hidden_dim,
            bias=False
        )


        self.down_proj = nn.Linear(
            hidden_dim,
            dim,
            bias=False
        )


    def forward(
        self,
        x
    ):

        gate = self.gate_proj(
            x
        )


        up = self.up_proj(
            x
        )


        hidden = (
            F.silu(
                gate
            )
            *
            up
        )


        output = self.down_proj(
            hidden
        )


        return output