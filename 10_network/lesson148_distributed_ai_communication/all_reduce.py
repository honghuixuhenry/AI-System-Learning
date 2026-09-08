def all_reduce_sum(
    values
):
    total = sum(values)

    return [
        total
        for _ in values
    ]


def all_reduce_mean(
    values
):
    mean = (
        sum(values)
        /
        len(values)
    )

    return [
        mean
        for _ in values
    ]