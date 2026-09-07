parameters = [
    "P0",
    "P1",
    "P2",
    "P3",
    "P4",
    "P5",
    "P6",
    "P7",
]


world_size = 4


shards = [
    parameters[
        rank::world_size
    ]
    for rank in range(
        world_size
    )
]


for rank, shard in enumerate(
    shards
):

    print(
        f"rank {rank}:",
        shard
    )