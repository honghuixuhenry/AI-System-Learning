def kv_cache_bytes(
    num_layers,
    num_kv_heads,
    head_dim,
    sequence_length,
    bytes_per_element,
    batch_size=1
):

    return (
        2
        * num_layers
        * num_kv_heads
        * head_dim
        * sequence_length
        * bytes_per_element
        * batch_size
    )


memory = kv_cache_bytes(
    num_layers=32,
    num_kv_heads=8,
    head_dim=128,
    sequence_length=4096,
    bytes_per_element=2
)


print(
    "Bytes:",
    memory
)

print(
    "MiB:",
    memory / (1024 ** 2)
)