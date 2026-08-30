import torch
import torch.nn as nn


loss_fn = nn.BCEWithLogitsLoss()


logits = torch.tensor(
    [
        [2.0],
        [-1.0],
        [0.3]
    ]
)


targets = torch.tensor(
    [
        [1.0],
        [0.0],
        [1.0]
    ]
)


loss = loss_fn(
    logits,
    targets
)


print(loss)