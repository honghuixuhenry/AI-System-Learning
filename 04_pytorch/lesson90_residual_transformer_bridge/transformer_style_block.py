import torch
import torch.nn as nn


class FakeAttention(nn.Module):

    def __init__(self, dim):

        super().__init__()

        self.projection = nn.Linear(
            dim,
            dim
        )


    def forward(self, x):

        return self.projection(x)


class TransformerStyleBlock(nn.Module):

    def __init__(
        self,
        dim,
        hidden_dim
    ):

        super().__init__()


        self.norm1 = nn.LayerNorm(
            dim
        )

        self.attention = FakeAttention(
            dim
        )


        self.norm2 = nn.LayerNorm(
            dim
        )

        self.ffn = nn.Sequential(

            nn.Linear(
                dim,
                hidden_dim
            ),

            nn.GELU(),

            nn.Linear(
                hidden_dim,
                dim
            )
        )


    def forward(self, x):

        x = x + self.attention(
            self.norm1(x)
        )

        x = x + self.ffn(
            self.norm2(x)
        )

        return x