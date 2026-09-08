def broadcast(
    values,
    source_rank
):
    source_value = values[
        source_rank
    ]

    return [
        source_value
        for _ in values
    ]


def reduce_sum(values):
    return sum(values)