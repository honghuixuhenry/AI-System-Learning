import torch
import torch.nn.functional as F


def train(
    model,
    dataloader,
    optimizer,
    scheduler,
    device,
    accumulation_steps=1,
    max_grad_norm=1.0,
):

    model.train()

    optimizer.zero_grad()

    optimizer_step = 0


    use_cuda = (
        device.type == "cuda"
    )


    scaler = (
        torch.amp.GradScaler(
            "cuda"
        )
        if use_cuda
        else None
    )


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


        if use_cuda:

            context = torch.autocast(
                device_type="cuda",
                dtype=torch.float16
            )

        else:

            context = (
                torch.autocast(
                    device_type="cpu",
                    dtype=torch.bfloat16
                )
            )


        with context:

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


        if not torch.isfinite(
            raw_loss
        ):

            raise RuntimeError(
                "Non-finite loss"
            )


        if scaler is not None:

            scaler.scale(
                loss
            ).backward()

        else:

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

            if scaler is not None:

                scaler.unscale_(
                    optimizer
                )


            grad_norm = (
                torch.nn.utils.clip_grad_norm_(
                    model.parameters(),
                    max_grad_norm
                )
            )


            if scaler is not None:

                scaler.step(
                    optimizer
                )

                scaler.update()

            else:

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