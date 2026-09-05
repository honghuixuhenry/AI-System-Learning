import torch


B = 2
T = 5


position_ids = torch.arange(
    T
)


print(
    "position ids:",
    position_ids
)

print(
    "shape:",
    position_ids.shape
)