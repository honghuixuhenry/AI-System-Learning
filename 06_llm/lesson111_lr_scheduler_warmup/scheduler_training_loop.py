import torch
import torch.nn.functional as F


def train(
    model,
    dataloader,
    optimizer,
    scheduler,
    device,
    epochs,
    accumulation_steps=1,
    max_grad_norm=1.0
):

    model.train()

    optimizer.zero_grad()

    optimizer_step = 0


    for epoch in range(epochs):

        for micro_step, (
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


            raw_loss = F.cross_entropy(
                logits.reshape(
                    -1,
                    vocab_size
                ),
                targets.reshape(-1)
            )


            loss = (
                raw_loss
                /
                accumulation_steps
            )


            loss.backward()


            should_update = (
                (
                    micro_step + 1
                )
                %
                accumulation_steps
                ==
                0
            )


            if should_update:

                grad_norm = (
                    torch.nn.utils.clip_grad_norm_(
                        model.parameters(),
                        max_grad_norm
                    )
                )


                optimizer.step()

                scheduler.step()

                optimizer.zero_grad()


                optimizer_step += 1


                lr = (
                    optimizer
                    .param_groups[0]["lr"]
                )


                print(
                    "step:",
                    optimizer_step,
                    "loss:",
                    raw_loss.item(),
                    "lr:",
                    lr,
                    "grad_norm:",
                    float(grad_norm)
                )