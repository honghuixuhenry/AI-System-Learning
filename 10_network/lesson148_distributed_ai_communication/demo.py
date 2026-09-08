from all_reduce import (
    all_reduce_mean
)

from broadcast_reduce import (
    broadcast,
    reduce_sum
)

from gather_scatter import (
    all_gather
)


gradients = [
    1.0,
    2.0,
    3.0,
    4.0
]


print(
    "Broadcast:",
    broadcast(
        gradients,
        source_rank=0
    )
)


print(
    "Reduce:",
    reduce_sum(
        gradients
    )
)


print(
    "All-Reduce:",
    all_reduce_mean(
        gradients
    )
)


print(
    "All-Gather:",
    all_gather(
        gradients
    )
)