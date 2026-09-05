import torch


logits = torch.tensor(
    [
        [0.2, 1.5, 0.7, 2.3]
    ]
)


next_token = torch.argmax(
    logits,
    dim=-1,
    keepdim=True
)


print(
    next_token
)