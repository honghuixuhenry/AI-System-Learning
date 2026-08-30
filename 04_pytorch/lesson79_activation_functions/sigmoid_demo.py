import torch
import torch.nn as nn


sigmoid = nn.Sigmoid()


x = torch.tensor(
    [-5., -1., 0., 1., 5.]
)


y = sigmoid(x)


print(y)