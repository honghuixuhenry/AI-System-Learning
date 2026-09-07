def kv_cache_bytes(
    batch_size,
    num_layers,
    num_kv_heads,
    sequence_length,
    head_dim,
    bytes_per_element
):

    return (
        batch_size
        *
        num_layers
        *
        2
        *
        num_kv_heads
        *
        sequence_length
        *
        head_dim
        *
        bytes_per_element
    )


def bytes_to_mib(num_bytes):
    return (
        num_bytes
        /
        (1024 ** 2)
    )


memory = kv_cache_bytes(
    batch_size=1,
    num_layers=32,
    num_kv_heads=8,
    sequence_length=4096,
    head_dim=128,
    bytes_per_element=2
)


print(
    round(
        bytes_to_mib(memory),
        2
    ),
    "MiB"
)