def weight_memory_bytes(
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


def bytes_to_gib(num_bytes):
    return (
        num_bytes
        /
        (1024 ** 3)
    )


models = {
    "7B": 7_000_000_000,
    "32B": 32_000_000_000,
    "70B": 70_000_000_000
}


for name, params in models.items():

    print(f"\n{name}")

    for bits in [16, 8, 4]:

        memory = weight_memory_bytes(
            params,
            bits
        )

        print(
            bits,
            "bit:",
            round(
                bytes_to_gib(memory),
                2
            ),
            "GiB"
        )