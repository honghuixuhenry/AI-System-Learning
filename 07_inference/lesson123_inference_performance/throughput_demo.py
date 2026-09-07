def output_throughput(
    total_output_tokens,
    total_time_seconds
):

    return (
        total_output_tokens
        /
        total_time_seconds
    )


tokens = 10000
seconds = 5


print(
    output_throughput(
        tokens,
        seconds
    ),
    "output tokens/s"
)