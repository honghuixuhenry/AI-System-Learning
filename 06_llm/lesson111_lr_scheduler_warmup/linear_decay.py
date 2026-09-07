def linear_decay_lr(
    step,
    warmup_steps,
    total_steps,
    peak_lr,
    min_lr=0.0
):

    if step < warmup_steps:

        return (
            peak_lr
            *
            step
            /
            max(
                warmup_steps,
                1
            )
        )


    decay_steps = (
        total_steps
        -
        warmup_steps
    )


    progress = (
        step
        -
        warmup_steps
    ) / max(
        decay_steps,
        1
    )


    progress = min(
        max(
            progress,
            0.0
        ),
        1.0
    )


    return (
        peak_lr
        -
        progress
        *
        (
            peak_lr
            -
            min_lr
        )
    )