import torch
import torch.nn as nn


class TinyLM(nn.Module):

    def __init__(
        self,
        vocab_size=1000,
        d_model=128
    ):

        super().__init__()

        self.embedding = nn.Embedding(
            vocab_size,
            d_model
        )

        self.lm_head = nn.Linear(
            d_model,
            vocab_size
        )


    def forward(self, token_ids):

        hidden = self.embedding(
            token_ids
        )

        logits = self.lm_head(
            hidden
        )

        return logits


model = TinyLM()


prompt = torch.tensor([
    [
        10,
        20,
        30,
        40
    ]
])


logits = model(
    prompt
)


print(
    "Prompt shape:",
    prompt.shape
)

print(
    "Logits shape:",
    logits.shape
)