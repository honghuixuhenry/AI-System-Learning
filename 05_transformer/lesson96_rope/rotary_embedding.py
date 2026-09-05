import torch
import torch.nn as nn


class RotaryEmbedding(
    nn.Module
):

    def __init__(
        self,
        head_dim,
        base=10000.0
    ):

        super().__init__()


        assert (
            head_dim % 2 == 0
        )


        self.head_dim = (
            head_dim
        )


        inv_freq = 1.0 / (
            base
            **
            (
                torch.arange(
                    0,
                    head_dim,
                    2
                ).float()
                /
                head_dim
            )
        )


        self.register_buffer(
            "inv_freq",
            inv_freq,
            persistent=False
        )


    def forward(
        self,
        seq_len,
        device
    ):

        positions = torch.arange(
            seq_len,
            device=device,
            dtype=self.inv_freq.dtype
        )


        inv_freq = self.inv_freq.to(
            device
        )


        angles = torch.outer(
            positions,
            inv_freq
        )


        cos = torch.cos(
            angles
        )

        sin = torch.sin(
            angles
        )


        return cos, sin