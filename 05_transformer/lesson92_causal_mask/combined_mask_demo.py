import torch


B = 2
T = 4


scores = torch.randn(
    B,
    T,
    T
)


causal_mask = torch.tril(
    torch.ones(
        T,
        T,
        dtype=torch.bool
    )
)


padding_mask = torch.tensor(
    [
        [1,1,1,1],
        [1,1,1,0]
    ],
    dtype=torch.bool
)


key_padding_mask = (
    padding_mask.unsqueeze(
        1
    )
)


scores = scores.masked_fill(
    ~causal_mask,
    float("-inf")
)


scores = scores.masked_fill(
    ~key_padding_mask,
    float("-inf")
)


weights = torch.softmax(
    scores,
    dim=-1
)


print(weights)