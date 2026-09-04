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


class Block(nn.Module):

    def __init__(
        self,
        dim,
        ffn_dim
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
                ffn_dim
            ),
            nn.GELU(),
            nn.Linear(
                ffn_dim,
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

class MiniTransformerSkeleton(
    nn.Module
):

    def __init__(
        self,
        vocab_size,
        dim=32,
        ffn_dim=128,
        num_layers=2
    ):

        super().__init__()


        self.embedding = nn.Embedding(
            vocab_size,
            dim
        )


        self.blocks = nn.ModuleList([
            Block(
                dim,
                ffn_dim
            )
            for _ in range(
                num_layers
            )
        ])


        self.final_norm = nn.LayerNorm(
            dim
        )


        self.lm_head = nn.Linear(
            dim,
            vocab_size
        )


    def forward(
        self,
        token_ids
    ):

        x = self.embedding(
            token_ids
        )


        for block in self.blocks:

            x = block(
                x
            )


        x = self.final_norm(
            x
        )


        logits = self.lm_head(
            x
        )


        return logits

model = MiniTransformerSkeleton(
    vocab_size=100
)


token_ids = torch.randint(
    0,
    100,
    (
        4,
        8
    )
)


logits = model(
    token_ids
)


print(
    token_ids.shape
)

print(
    logits.shape
)

B, T, V = logits.shape


loss = nn.CrossEntropyLoss()(
    logits.reshape(
        B * T,
        V
    ),

    targets.reshape(
        B * T
    )
)
