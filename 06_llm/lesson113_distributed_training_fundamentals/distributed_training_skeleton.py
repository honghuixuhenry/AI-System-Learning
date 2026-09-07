def distributed_training_step(
    model,
    batch,
    optimizer,
    rank,
    world_size
):

    input_ids, targets = batch


    # Each rank runs forward
    logits = model(
        input_ids
    )


    # Each rank computes local loss
    loss = compute_loss(
        logits,
        targets
    )


    # Each rank computes local gradients
    loss.backward()


    # Conceptually:
    #
    # all_reduce_gradients(
    #     model.parameters(),
    #     world_size
    # )
    #
    # DDP will automate this.


    optimizer.step()

    optimizer.zero_grad()


    if rank == 0:
        print(
            "loss:",
            loss.item()
        )