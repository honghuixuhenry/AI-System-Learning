def all_gather(
    local_values
):
    gathered = list(
        local_values
    )

    return [
        gathered.copy()
        for _ in local_values
    ]


def scatter(
    values
):
    return list(values)