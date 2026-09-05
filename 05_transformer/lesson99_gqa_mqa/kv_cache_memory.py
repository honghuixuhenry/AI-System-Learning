def kv_cache_bytes(
    num_layers,
    batch_size,
    seq_len,
    num_kv_heads,
    head_dim,
    bytes_per_element=2
):

    num_elements = (
        2
        *
        num_layers
        *
        batch_size
        *
        seq_len
        *
        num_kv_heads
        *
        head_dim
    )


    return (
        num_elements
        *
        bytes_per_element
    )