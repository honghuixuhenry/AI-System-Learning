import torch
import torch.nn as nn


class MiniGPT(nn.Module):

    def __init__(
        self,
        vocab_size,
        max_seq_len,
        dim,
        num_heads,
        ffn_hidden_dim,
        num_layers
    ):

        super().__init__()


        self.max_seq_len = (
            max_seq_len
        )


        self.token_embedding = (
            nn.Embedding(
                vocab_size,
                dim
            )
        )


        self.position_embedding = (
            nn.Embedding(
                max_seq_len,
                dim
            )
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

        B, T = token_ids.shape


        if T > self.max_seq_len:

            raise ValueError(
                "Sequence is longer "
                "than max_seq_len"
            )


        token_vectors = (
            self.token_embedding(
                token_ids
            )
        )


        position_ids = (
            torch.arange(
                T,
                device=token_ids.device
            )
        )


        position_vectors = (
            self.position_embedding(
                position_ids
            )
        )


        x = (
            token_vectors
            +
            position_vectors
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