import torch
import torch.nn as nn


torch.manual_seed(
    42
)


dropout = nn.Dropout(
    p=0.5
)


x = torch.ones(
    10
)


dropout.train()

print(
    dropout(x)
)

print(
    dropout(x)
)