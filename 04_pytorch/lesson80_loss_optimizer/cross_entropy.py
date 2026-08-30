import torch
import torch.nn as nn


loss_fn = nn.CrossEntropyLoss()


logits = torch.tensor(
    [
        [2.0, 1.0, 0.1],
        [0.5, 2.2, 0.3]
    ]
)


target = torch.tensor(
    [0, 1]
)


loss = loss_fn(
    logits,
    target
)


print(loss)