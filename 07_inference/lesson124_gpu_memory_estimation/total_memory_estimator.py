def gib(num_bytes):
    return (
        num_bytes
        /
        (1024 ** 3)
    )


def weight_bytes(
    num_parameters,
    bits_per_parameter
):
    return (
        num_parameters
        *
        bits_per_parameter
        /
        8
    )


def kv_bytes(
    batch_size,
    layers,
    kv_heads,
    sequence_length,
    head_dim,
    bytes_per_element
):
    return (
        batch_size
        *
        layers
        *
        2
        *
        kv_heads
        *
        sequence_length
        *
        head_dim
        *
        bytes_per_element
    )


weights = weight_bytes(
    num_parameters=7_000_000_000,
    bits_per_parameter=4
)


kv = kv_bytes(
    batch_size=8,
    layers=32,
    kv_heads=8,
    sequence_length=4096,
    head_dim=128,
    bytes_per_element=2
)


activation_estimate = (
    1.0
    *
    1024 ** 3
)


runtime_estimate = (
    1.0
    *
    1024 ** 3
)


total = (
    weights
    +
    kv
    +
    activation_estimate
    +
    runtime_estimate
)


print(
    "Weights:",
    round(gib(weights), 2),
    "GiB"
)


print(
    "KV Cache:",
    round(gib(kv), 2),
    "GiB"
)


print(
    "Total Estimate:",
    round(gib(total), 2),
    "GiB"
)