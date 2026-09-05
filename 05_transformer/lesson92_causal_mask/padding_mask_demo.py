import torch


B = 2
T = 3


scores = torch.randn(
    B,
    T,
    T
)


padding_mask = torch.tensor(
    [
        [1, 1, 1],
        [1, 1, 0]
    ],
    dtype=torch.bool
)


key_mask = padding_mask.unsqueeze(
    1
)


masked_scores = scores.masked_fill(
    ~key_mask,
    float("-inf")
)


weights = torch.softmax(
    masked_scores,
    dim=-1
)


print(
    weights
)