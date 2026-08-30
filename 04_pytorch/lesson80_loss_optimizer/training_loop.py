import torch
import torch.nn as nn


class Model(
    nn.Module
):

    def __init__(self):

        super().__init__()

        self.network = nn.Sequential(

            nn.Linear(
                1,
                8
            ),

            nn.ReLU(),

            nn.Linear(
                8,
                1
            )
        )

    def forward(
        self,
        x
    ):

        return self.network(x)


model = Model()


loss_fn = nn.MSELoss()


optimizer = torch.optim.Adam(
    model.parameters(),
    lr=0.01
)


x = torch.tensor(
    [[1.], [2.], [3.], [4.]]
)

target = torch.tensor(
    [[3.], [5.], [7.], [9.]]
)


for epoch in range(500):

    optimizer.zero_grad()

    prediction = model(x)

    loss = loss_fn(
        prediction,
        target
    )

    loss.backward()

    optimizer.step()


    if epoch % 50 == 0:

        print(
            epoch,
            loss.item()
        )