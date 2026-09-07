import torch
import torch.nn.functional as F


logits = torch.tensor(
    [
        [1.0, 2.0, 5.0],
        [4.0, 1.0, 0.5]
    ]
)

targets = torch.tensor(
    [
        2,
        0
    ],
    dtype=torch.long
)


loss_per_token = F.cross_entropy(
    logits,
    targets,
    reduction="none"
)


print(
    loss_per_token
)