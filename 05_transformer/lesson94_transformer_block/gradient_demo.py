import torch
import torch.nn as nn


B = 2
T = 8
D = 32


x = torch.randn(
    B,
    T,
    D
)


model = TransformerBlock(
    dim=32,
    num_heads=4,
    ffn_hidden_dim=128
)


output = model(
    x
)


loss = output.pow(
    2
).mean()


loss.backward()


for name, param in (
    model.named_parameters()
):

    if param.grad is not None:

        print(
            name,
            param.grad.norm().item()
        )