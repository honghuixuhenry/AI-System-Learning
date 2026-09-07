import torch
import torch.nn as nn


class MiniLLM(nn.Module):

    def __init__(
        self,
        vocab_size,
        d_model,
        num_heads,
        num_layers
    ):

        super().__init__()

        self.embedding = nn.Embedding(
            vocab_size,
            d_model
        )

        layer = nn.TransformerEncoderLayer(
            d_model=d_model,
            nhead=num_heads,
            dim_feedforward=4 * d_model,
            batch_first=True,
            norm_first=True
        )

        self.transformer = (
            nn.TransformerEncoder(
                layer,
                num_layers=num_layers
            )
        )

        self.lm_head = nn.Linear(
            d_model,
            vocab_size,
            bias=False
        )


    def forward(
        self,
        token_ids,
        causal_mask
    ):

        x = self.embedding(
            token_ids
        )

        x = self.transformer(
            x,
            mask=causal_mask,
            is_causal=True
        )

        logits = self.lm_head(
            x
        )

        return logits