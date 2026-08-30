import torch
import torch.nn as nn


gelu = nn.GELU()


x = torch.tensor(
    [-2., -1., 0., 1., 2.]
)


y = gelu(x)


print(y)