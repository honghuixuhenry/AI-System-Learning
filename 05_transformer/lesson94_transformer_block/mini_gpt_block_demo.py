import torch
import torch.nn as nn


class MiniGPTSkeleton(
    nn.Module
):

    def __init__(
        self,
        vocab_size,
        dim,
        num_heads,
        ffn_hidden_dim,
        num_layers
    ):

        super().__init__()


        self.embedding = nn.Embedding(
            vocab_size,
            dim
        )


        self.blocks = nn.ModuleList([
            TransformerBlock(
                dim=dim,
                num_heads=num_heads,
                ffn_hidden_dim=ffn_hidden_dim
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