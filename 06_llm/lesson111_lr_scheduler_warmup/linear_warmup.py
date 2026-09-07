def linear_warmup_lr(
    step,
    warmup_steps,
    peak_lr
):

    if warmup_steps <= 0:
        return peak_lr


    progress = (
        step
        /
        warmup_steps
    )


    progress = min(
        progress,
        1.0
    )


    return (
        peak_lr
        *
        progress
    )

peak_lr = 3e-4

warmup_steps = 1000


for step in [
    0,
    250,
    500,
    750,
    1000
]:

    lr = linear_warmup_lr(
        step,
        warmup_steps,
        peak_lr
    )

    print(
        step,
        lr
    )