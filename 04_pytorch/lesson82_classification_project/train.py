num_epochs = 50


for epoch in range(
    num_epochs
):

    train_loss, train_acc = (
        train_one_epoch(
            model,
            train_loader,
            loss_fn,
            optimizer,
            device
        )
    )


    val_loss, val_acc = (
        evaluate(
            model,
            val_loader,
            loss_fn,
            device
        )
    )


    print(
        f"Epoch {epoch + 1:02d} | "
        f"Train Loss: {train_loss:.4f} | "
        f"Train Acc: {train_acc:.2%} | "
        f"Val Loss: {val_loss:.4f} | "
        f"Val Acc: {val_acc:.2%}"
    )