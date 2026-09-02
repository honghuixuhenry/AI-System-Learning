def accuracy(
    logits,
    labels
):

    predictions = logits.argmax(
        dim=1
    )

    correct = (
        predictions
        ==
        labels
    ).sum().item()

    total = labels.size(
        0
    )

    return (
        correct,
        total
    )