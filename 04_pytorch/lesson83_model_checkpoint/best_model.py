best_val_loss = float(
    "inf"
)


for epoch in range(
    num_epochs
):

    train_loss, train_acc = (
        train_one_epoch(...)
    )

    val_loss, val_acc = (
        evaluate(...)
    )


    if val_loss < best_val_loss:

        best_val_loss = val_loss

        torch.save(
            model.state_dict(),
            "checkpoints/best_model.pt"
        )

        print(
            "Saved new best model"
        )