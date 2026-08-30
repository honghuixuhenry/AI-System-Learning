import torch
import torch.nn as nn


tanh = nn.Tanh()


x = torch.tensor(
    [-5., -1., 0., 1., 5.]
)


y = tanh(x)


print(y)