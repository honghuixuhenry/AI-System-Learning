import torch
import torch.nn as nn


relu = nn.ReLU()


x = torch.tensor(
    [-2., -1., 0., 1., 2.]
)


y = relu(x)


print(y)