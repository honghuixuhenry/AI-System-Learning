import torch
from lora_linear import LoRALinear


model = LoRALinear(
    in_features=128,
    out_features=128,
    rank=8,
    alpha=16
)


optimizer = torch.optim.AdamW(
    [
        p
        for p in model.parameters()
        if p.requires_grad
    ],
    lr=1e-3
)


x = torch.randn(
    16,
    128
)

target = torch.randn(
    16,
    128
)


output = model(
    x
)


loss = torch.nn.functional.mse_loss(
    output,
    target
)


optimizer.zero_grad()

loss.backward()

optimizer.step()


print(
    "loss:",
    loss.item()
)