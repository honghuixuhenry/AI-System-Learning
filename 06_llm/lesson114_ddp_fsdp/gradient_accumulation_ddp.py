from contextlib import nullcontext


accumulation_steps = 4


optimizer.zero_grad()


for micro_step, (
    input_ids,
    targets
) in enumerate(
    dataloader
):

    is_update_step = (
        (
            micro_step + 1
        )
        %
        accumulation_steps
        ==
        0
    )


    sync_context = (
        nullcontext()
        if is_update_step
        else model.no_sync()
    )


    with sync_context:

        logits = model(
            input_ids
        )


        raw_loss = (
            compute_loss(
                logits,
                targets
            )
        )


        loss = (
            raw_loss
            /
            accumulation_steps
        )


        loss.backward()


    if is_update_step:

        optimizer.step()

        optimizer.zero_grad()