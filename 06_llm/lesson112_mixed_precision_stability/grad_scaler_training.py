import torch
import torch.nn.functional as F


scaler = torch.amp.GradScaler(
    "cuda"
)


optimizer.zero_grad()


for input_ids, targets in dataloader:

    input_ids = input_ids.to(
        device
    )

    targets = targets.to(
        device
    )


    with torch.autocast(
        device_type="cuda",
        dtype=torch.float16
    ):

        logits = model(
            input_ids
        )


        vocab_size = (
            logits.size(-1)
        )


        loss = F.cross_entropy(
            logits.reshape(
                -1,
                vocab_size
            ),
            targets.reshape(-1)
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


    optimizer.zero_grad()