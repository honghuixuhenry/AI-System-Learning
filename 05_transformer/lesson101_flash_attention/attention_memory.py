def attention_matrix_bytes(
    batch_size,
    num_heads,
    seq_len,
    bytes_per_element=2
):
    num_elements = (
        batch_size
        *
        num_heads
        *
        seq_len
        *
        seq_len
    )

    return (
        num_elements
        *
        bytes_per_element
    )


for seq_len in [
    1024,
    2048,
    4096,
    8192
]:
    size_bytes = attention_matrix_bytes(
        batch_size=1,
        num_heads=32,
        seq_len=seq_len,
        bytes_per_element=2
    )

    size_gib = (
        size_bytes
        /
        1024**3
    )

    print(
        seq_len,
        f"{size_gib:.3f} GiB"
    )