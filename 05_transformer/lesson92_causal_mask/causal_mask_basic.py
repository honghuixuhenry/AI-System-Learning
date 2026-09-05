import torch


T = 5


mask = torch.tril(
    torch.ones(
        T,
        T,
        dtype=torch.bool
    )
)


print(mask)

print(
    mask.shape
)