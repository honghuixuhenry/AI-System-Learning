import math


def cosine_lr(
    step,
    warmup_steps,
    total_steps,
    peak_lr,
    min_lr=0.0
):

    # ----------------------
    # Warmup
    # ----------------------

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


    # ----------------------
    # After training end
    # ----------------------

    if step >= total_steps:

        return min_lr


    # ----------------------
    # Cosine decay
    # ----------------------

    decay_steps = (
        total_steps
        -
        warmup_steps
    )


    decay_progress = (
        step
        -
        warmup_steps
    ) / decay_steps


    cosine_value = (
        0.5
        *
        (
            1.0
            +
            math.cos(
                math.pi
                *
                decay_progress
            )
        )
    )


    return (
        min_lr
        +
        cosine_value
        *
        (
            peak_lr
            -
            min_lr
        )
    )