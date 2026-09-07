accumulation_steps = 4


optimizer.zero_grad()


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


    scaled_loss = (
        loss
        /
        accumulation_steps
    )


    scaled_loss.backward()


    should_update = (
        (step + 1)
        %
        accumulation_steps
        ==
        0
    )


    if should_update:

        torch.nn.utils.clip_grad_norm_(
            model.parameters(),
            max_norm=1.0
        )


        optimizer.step()

        optimizer.zero_grad()