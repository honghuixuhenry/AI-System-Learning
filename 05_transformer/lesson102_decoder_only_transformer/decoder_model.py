import torch
import torch.nn as nn


class DecoderOnlyTransformer(
    nn.Module
):

    def __init__(
        self,
        config
    ):

        super().__init__()

        self.config = config


        self.token_embedding = (
            nn.Embedding(
                config.vocab_size,
                config.dim
            )
        )


        self.layers = nn.ModuleList(
            [
                TransformerBlock(
                    config
                )
                for _ in range(
                    config.num_layers
                )
            ]
        )


        self.final_norm = RMSNorm(
            config.dim,
            eps=config.rms_eps
        )


        self.lm_head = nn.Linear(
            config.dim,
            config.vocab_size,
            bias=False
        )
    