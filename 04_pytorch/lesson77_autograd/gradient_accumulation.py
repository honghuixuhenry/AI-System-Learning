import torch


x = torch.tensor(
    2.0,
    requires_grad=True
)


y = x ** 2

y.backward()

print(
    "first:",
    x.grad
)


y = x ** 2

y.backward()

print(
    "second:",
    x.grad
)


x.grad.zero_()


print(
    "after zero:",
    x.grad
)