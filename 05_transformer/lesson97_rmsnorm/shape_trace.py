import torch


B = 2
T = 3
D = 4


x = torch.randn(
    B,
    T,
    D
)


mean_square = (
    x.pow(2).mean(
        dim=-1,
        keepdim=True
    )
)


rms = torch.sqrt(
    mean_square
    +
    1e-6
)


normalized = (
    x / rms
)


print(
    "x:",
    x.shape
)

print(
    "mean square:",
    mean_square.shape
)

print(
    "rms:",
    rms.shape
)

print(
    "normalized:",
    normalized.shape
)