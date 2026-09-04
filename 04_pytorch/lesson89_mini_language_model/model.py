import torch.nn as nn


class MiniLanguageModel(
    nn.Module
):

    def __init__(
        self,
        vocab_size,
        embedding_dim=16,
        hidden_dim=32
    ):

        super().__init__()


        self.embedding = nn.Embedding(
            vocab_size,
            embedding_dim
        )


        self.network = nn.Sequential(

            nn.Linear(
                embedding_dim,
                hidden_dim
            ),

            nn.ReLU(),

            nn.Linear(
                hidden_dim,
                vocab_size
            )
        )


    def forward(
        self,
        token_ids
    ):

        x = self.embedding(
            token_ids
        )

        logits = self.network(
            x
        )

        return logits