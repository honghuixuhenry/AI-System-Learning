import torch
import torch.nn as nn

from feed_forward import FeedForward
from causal_multi_head_attention import (
    CausalMultiHeadAttention
)


class TransformerBlock(
    nn.Module
):

    def __init__(
        self,
        dim,
        num_heads,
        ffn_hidden_dim,
        dropout=0.0
    ):

        super().__init__()


        self.norm1 = nn.LayerNorm(
            dim
        )

        self.attention = (
            CausalMultiHeadAttention(
                dim,
                num_heads
            )
        )


        self.norm2 = nn.LayerNorm(
            dim
        )

        self.ffn = FeedForward(
            dim,
            ffn_hidden_dim,
            dropout
        )


    def forward(
        self,
        x
    ):

        attention_output, _ = (
            self.attention(
                self.norm1(
                    x
                )
            )
        )


        x = (
            x
            +
            attention_output
        )


        ffn_output = self.ffn(
            self.norm2(
                x
            )
        )


        x = (
            x
            +
            ffn_output
        )


        return x