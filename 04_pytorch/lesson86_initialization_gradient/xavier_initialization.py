import torch.nn as nn


layer = nn.Linear(
    128,
    64
)


nn.init.xavier_uniform_(
    layer.weight
)


nn.init.zeros_(
    layer.bias
)


print(
    layer.weight.mean()
)

print(
    layer.weight.std()
)