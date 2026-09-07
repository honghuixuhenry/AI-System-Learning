import torch
import torch.nn.functional as F


def train_one_epoch(
    model,
    dataloader,
    optimizer,
    device,
    accumulation_steps=1,
    max_grad_norm=1.0
):

    model.train()

    optimizer.zero_grad()


    total_loss = 0.0

    total_tokens = 0


    for step, (
        input_ids,
        targets
    ) in enumerate(dataloader):

        input_ids = input_ids.to(
            device
        )

        targets = targets.to(
            device
        )


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


        batch_tokens = (
            targets.numel()
        )


        total_loss += (
            loss.item()
            *
            batch_tokens
        )


        total_tokens += (
            batch_tokens
        )


        scaled_loss = (
            loss
            /
            accumulation_steps
        )


        scaled_loss.backward()


        should_update = (
            (
                (step + 1)
                %
                accumulation_steps
                ==
                0
            )
            or
            (
                step + 1
                ==
                len(dataloader)
            )
        )


        if should_update:

            torch.nn.utils.clip_grad_norm_(
                model.parameters(),
                max_grad_norm
            )


            optimizer.step()

            optimizer.zero_grad()


    average_loss = (
        total_loss
        /
        total_tokens
    )


    return average_loss