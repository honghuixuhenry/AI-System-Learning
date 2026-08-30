import torch
import torch.nn as nn


loss_fn = nn.MSELoss()


prediction = torch.tensor(
    [2., 4., 6.]
)

target = torch.tensor(
    [3., 5., 7.]
)


loss = loss_fn(
    prediction,
    target
)


print(loss)