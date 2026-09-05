import torch


head_dim = 8
base = 10000.0


inv_freq = 1.0 / (
    base
    **
    (
        torch.arange(
            0,
            head_dim,
            2
        ).float()
        /
        head_dim
    )
)


print(
    inv_freq
)

print(
    inv_freq.shape
)