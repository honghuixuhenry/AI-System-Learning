import torch


x = torch.tensor(
    2.0,
    requires_grad=True
)


y = x * 3


print(
    y.requires_grad
)


with torch.no_grad():

    z = x * 3


print(
    z.requires_grad
)