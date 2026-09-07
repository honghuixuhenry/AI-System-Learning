def model_weight_memory(
    num_parameters,
    bits_per_parameter
):

    total_bits = (
        num_parameters
        *
        bits_per_parameter
    )

    total_bytes = (
        total_bits / 8
    )

    gib = (
        total_bytes
        /
        (1024 ** 3)
    )

    return gib


parameters = 7_000_000_000


for bits in [
    32,
    16,
    8,
    4
]:

    memory = model_weight_memory(
        parameters,
        bits
    )

    print(
        bits,
        "bits:",
        memory,
        "GiB"
    )