import torch

x = torch.tensor(
    2.0,
    requires_grad = True
)

a = x * 3
b = a + 2
y = b ** 2

print("x =", x)
print("a = ", a)
print("b = ", b)
print("y = ", y)

y.backward()
print(
    "dy/dx = ", x.grad
)