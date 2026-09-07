def effective_batch_size(
    micro_batch_size,
    accumulation_steps,
    world_size=1
):

    return (
        micro_batch_size
        *
        accumulation_steps
        *
        world_size
    )


batch_size = (
    effective_batch_size(
        micro_batch_size=8,
        accumulation_steps=4,
        world_size=8
    )
)


print(
    batch_size
)