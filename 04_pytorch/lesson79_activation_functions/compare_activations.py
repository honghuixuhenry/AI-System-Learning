import torch
import torch.nn as nn


x = torch.tensor(
    [-3., -1., 0., 1., 3.]
)


activations = {
    "ReLU": nn.ReLU(),
    "Sigmoid": nn.Sigmoid(),
    "Tanh": nn.Tanh(),
    "GELU": nn.GELU()
}


for name, activation in (
    activations.items()
):

    y = activation(x)

    print(
        name,
        y
    )