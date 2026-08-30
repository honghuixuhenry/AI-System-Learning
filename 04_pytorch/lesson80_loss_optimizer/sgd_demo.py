import torch
import torch.nn as nn


model = nn.Linear(
    1,
    1
)


optimizer = torch.optim.SGD(
    model.parameters(),
    lr=0.01
)


loss_fn = nn.MSELoss()


x = torch.tensor(
    [[1.], [2.], [3.], [4.]]
)

target = torch.tensor(
    [[2.], [4.], [6.], [8.]]
)


for epoch in range(100):

    optimizer.zero_grad()

    prediction = model(x)

    loss = loss_fn(
        prediction,
        target
    )

    loss.backward()

    optimizer.step()


print(
    model.weight
)

print(
    model.bias
)