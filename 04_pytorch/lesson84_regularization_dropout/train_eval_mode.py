import torch
import torch.nn as nn


model = nn.Sequential(

    nn.Linear(
        4,
        4
    ),

    nn.ReLU(),

    nn.Dropout(
        p=0.5
    )
)


x = torch.ones(
    1,
    4
)