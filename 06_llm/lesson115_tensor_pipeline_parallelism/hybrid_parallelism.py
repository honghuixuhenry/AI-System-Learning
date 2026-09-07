def total_gpus(
    data_parallel,
    tensor_parallel,
    pipeline_parallel
):

    return (
        data_parallel
        *
        tensor_parallel
        *
        pipeline_parallel
    )


dp = 8
tp = 4
pp = 2


print(
    total_gpus(
        dp,
        tp,
        pp
    )
)