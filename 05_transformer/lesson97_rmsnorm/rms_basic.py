import torch


x = torch.tensor([
    1.0,
    2.0,
    3.0
])


mean_square = (
    x.pow(2).mean()
)


rms = torch.sqrt(
    mean_square
)


normalized = (
    x / rms
)


print(
    "x:",
    x
)

print(
    "mean square:",
    mean_square
)

print(
    "rms:",
    rms
)

print(
    "normalized:",
    normalized
)