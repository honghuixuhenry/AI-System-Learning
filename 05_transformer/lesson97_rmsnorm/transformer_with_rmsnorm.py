import torch
import torch.nn as nn


class TransformerBlock(
    nn.Module
):

    def __init__(
        self,
        dim,
        num_heads,
        ffn_hidden_dim
    ):

        super().__init__()


        self.attn_norm = RMSNorm(
            dim
        )


        self.attention = (
            RoPECausalMultiHeadAttention(
                dim=dim,
                num_heads=num_heads
            )
        )


        self.ffn_norm = RMSNorm(
            dim
        )


        self.ffn = FeedForward(
            dim=dim,
            hidden_dim=ffn_hidden_dim
        )


    def forward(
        self,
        x
    ):

        attn_output = self.attention(
            self.attn_norm(
                x
            )
        )


        x = (
            x
            +
            attn_output
        )


        ffn_output = self.ffn(
            self.ffn_norm(
                x
            )
        )


        x = (
            x
            +
            ffn_output
        )


        return x