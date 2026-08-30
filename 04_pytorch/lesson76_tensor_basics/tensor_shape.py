import torch


x = torch.arange(
    12
)

print(
    "original:",
    x
)

print(
    "shape:",
    x.shape
)


y = x.reshape(
    3,
    4
)

print(
    "reshape:"
)

print(y)

print(
    y.shape
)


z = y.transpose(
    0,
    1
)

print(
    "transpose:"
)

print(z)

print(
    z.shape
)