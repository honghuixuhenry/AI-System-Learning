import torch


scores = torch.tensor([
    [
        [1.0, 2.0, 3.0],
        [4.0, 5.0, 6.0],
        [7.0, 8.0, 9.0]
    ]
])


T = scores.size(
    -1
)


mask = torch.tril(
    torch.ones(
        T,
        T,
        dtype=torch.bool
    )
)


masked_scores = scores.masked_fill(
    ~mask,
    float("-inf")
)


print(
    "original:"
)

print(scores)


print(
    "masked:"
)

print(masked_scores)