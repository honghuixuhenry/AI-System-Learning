import math


requests = [
    100,
    900,
    1500,
    50
]


max_length = 4096
block_size = 16


contiguous_allocated = (
    len(requests)
    *
    max_length
)


paged_allocated = sum(
    math.ceil(
        length / block_size
    )
    *
    block_size
    for length in requests
)


actual_tokens = sum(
    requests
)


print(
    "Actual tokens:",
    actual_tokens
)

print(
    "Max allocation:",
    contiguous_allocated
)

print(
    "Paged allocation:",
    paged_allocated
)