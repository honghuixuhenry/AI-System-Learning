import torch
import torch.nn as nn


class LoRALinear(nn.Module):

    def __init__(
        self,
        in_features,
        out_features,
        rank=4,
        alpha=1.0
    ):

        super().__init__()

        self.base = nn.Linear(
            in_features,
            out_features
        )

        for parameter in self.base.parameters():

            parameter.requires_grad = False


        self.lora_a = nn.Linear(
            in_features,
            rank,
            bias=False
        )

        self.lora_b = nn.Linear(
            rank,
            out_features,
            bias=False
        )


        nn.init.normal_(
            self.lora_a.weight,
            std=0.02
        )

        nn.init.zeros_(
            self.lora_b.weight
        )


        self.scale = alpha / rank


    def forward(self, x):

        base_output = self.base(
            x
        )

        lora_output = self.lora_b(
            self.lora_a(x)
        )

        return (
            base_output
            +
            self.scale
            *
            lora_output
        )