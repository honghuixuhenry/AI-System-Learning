import torch


def save_checkpoint(
    path,
    model,
    optimizer,
    global_step,
    scheduler=None,
    scaler=None
):

    checkpoint = {
        "model":
            model.state_dict(),

        "optimizer":
            optimizer.state_dict(),

        "global_step":
            global_step
    }


    if scheduler is not None:

        checkpoint[
            "scheduler"
        ] = scheduler.state_dict()


    if scaler is not None:

        checkpoint[
            "scaler"
        ] = scaler.state_dict()


    torch.save(
        checkpoint,
        path
    )