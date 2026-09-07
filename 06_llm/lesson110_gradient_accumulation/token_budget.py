def tokens_per_update(
    micro_batch_size,
    seq_len,
    accumulation_steps,
    world_size=1
):

    return (
        micro_batch_size
        *
        seq_len
        *
        accumulation_steps
        *
        world_size
    )


tokens = tokens_per_update(
    micro_batch_size=8,
    seq_len=2048,
    accumulation_steps=4,
    world_size=8
)


print(
    tokens
)