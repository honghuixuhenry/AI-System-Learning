import torch
import torch.nn as nn


device = torch.device(
    "cuda"
)


model = nn.Sequential(
    nn.Linear(
        100,
        256
    ),
    nn.ReLU(),
    nn.Linear(
        256,
        10
    )
).to(
    device
)


optimizer = torch.optim.AdamW(
    model.parameters(),
    lr=1e-3
)


loss_fn = nn.CrossEntropyLoss()


scaler = torch.amp.GradScaler(
    "cuda"
)

for x, y in loader:

    x = x.to(
        device
    )

    y = y.to(
        device
    )

    optimizer.zero_grad()


    with torch.autocast(
        device_type="cuda",
        dtype=torch.float16
    ):

        logits = model(
            x
        )

        loss = loss_fn(
            logits,
            y
        )


    scaler.scale(
        loss
    ).backward()


    scaler.unscale_(
        optimizer
    )


    torch.nn.utils.clip_grad_norm_(
        model.parameters(),
        1.0
    )


    scaler.step(
        optimizer
    )


    scaler.update()