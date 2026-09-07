def tensor_memory_bytes(
    shape,
    bytes_per_element
):

    num_elements = 1

    for dimension in shape:
        num_elements *= dimension

    return (
        num_elements
        *
        bytes_per_element
    )


shape = (
    1,
    4096,
    4096
)


memory = tensor_memory_bytes(
    shape,
    bytes_per_element=2
)


print(
    memory / (1024 ** 2),
    "MiB"
)