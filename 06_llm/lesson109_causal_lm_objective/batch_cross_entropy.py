import torch
import torch.nn.functional as F


B = 2
T = 4
V = 10


logits = torch.randn(
    B,
    T,
    V
)


targets = torch.randint(
    0,
    V,
    (
        B,
        T
    )
)


print(
    "logits:",
    logits.shape
)

print(
    "targets:",
    targets.shape
)

loss = F.cross_entropy(
    logits.reshape(
        B * T,
        V
    ),
    targets.reshape(
        B * T
    )
)