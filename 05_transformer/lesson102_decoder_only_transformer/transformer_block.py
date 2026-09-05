class RMSNorm(nn.Module):

    def __init__(
        self,
        dim,
        eps=1e-6
    ):

        super().__init__()

        self.weight = nn.Parameter(
            torch.ones(dim)
        )

        self.eps = eps


    def forward(
        self,
        x
    ):

        input_dtype = x.dtype

        x_float = x.float()

        rms = torch.rsqrt(
            x_float
            .pow(2)
            .mean(
                dim=-1,
                keepdim=True
            )
            +
            self.eps
        )

        output = (
            x_float
            *
            rms
        )

        return (
            self.weight
            *
            output.to(
                input_dtype
            )
        )

import torch.nn as nn


class TransformerBlock(
    nn.Module
):

    def __init__(
        self,
        config
    ):

        super().__init__()

        self.attn_norm = RMSNorm(
            config.dim,
            eps=config.rms_eps
        )

        self.attention = (
            CausalGQAAttention(
                config
            )
        )

        self.ffn_norm = RMSNorm(
            config.dim,
            eps=config.rms_eps
        )

        self.ffn = SwiGLU(
            config.dim,
            config.hidden_dim
        )


    def forward(
        self,
        x
    ):

        x = (
            x
            +
            self.attention(
                self.attn_norm(
                    x
                )
            )
        )

        x = (
            x
            +
            self.ffn(
                self.ffn_norm(
                    x
                )
            )
        )

        return x