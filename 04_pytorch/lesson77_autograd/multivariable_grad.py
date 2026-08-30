import torch


x = torch.tensor(
    2.0,
    requires_grad=True
)

y = torch.tensor(
    3.0,
    requires_grad=True
)


z = (
    x ** 2
    +
    y ** 3
)


z.backward()


print(
    "dz/dx:",
    x.grad
)

print(
    "dz/dy:",
    y.grad
)