import torch


B = 2
T = 5
D = 8
H = 2


head_dim = D // H


x = torch.randn(
    B,
    T,
    D
)


print(
    "original:",
    x.shape
)


x = x.reshape(
    B,
    T,
    H,
    head_dim
)


print(
    "after reshape:",
    x.shape
)


x = x.transpose(
    1,
    2
)


print(
    "after transpose:",
    x.shape
)