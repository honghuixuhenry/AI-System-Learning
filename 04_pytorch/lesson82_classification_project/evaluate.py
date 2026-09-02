def evaluate(
    model,
    loader,
    loss_fn,
    device
):

    model.eval()

    total_loss = 0.0
    total_correct = 0
    total_samples = 0


    with torch.no_grad():

        for x_batch, labels in loader:

            x_batch = x_batch.to(
                device
            )

            labels = labels.to(
                device
            )


            logits = model(
                x_batch
            )


            loss = loss_fn(
                logits,
                labels
            )


            batch_size = labels.size(
                0
            )


            total_loss += (
                loss.item()
                *
                batch_size
            )


            predictions = (
                logits.argmax(
                    dim=1
                )
            )


            total_correct += (
                predictions
                ==
                labels
            ).sum().item()


            total_samples += (
                batch_size
            )


    average_loss = (
        total_loss
        /
        total_samples
    )


    accuracy = (
        total_correct
        /
        total_samples
    )


    return (
        average_loss,
        accuracy
    )