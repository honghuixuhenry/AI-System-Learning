import torch


model = torch.nn.Linear(
    10,
    10
)


optimizer = torch.optim.AdamW(
    model.parameters(),
    lr=3e-4
)


for step in range(5):

    lr = (
        optimizer
        .param_groups[0]["lr"]
    )

    print(
        step,
        lr
    )