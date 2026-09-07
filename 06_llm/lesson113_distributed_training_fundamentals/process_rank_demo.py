def describe_process(
    rank,
    local_rank,
    world_size,
    node_id
):
    print(
        f"node={node_id}, "
        f"rank={rank}, "
        f"local_rank={local_rank}, "
        f"world_size={world_size}"
    )


world_size = 8


for rank in range(world_size):

    gpus_per_node = 4

    node_id = (
        rank
        //
        gpus_per_node
    )

    local_rank = (
        rank
        %
        gpus_per_node
    )


    describe_process(
        rank,
        local_rank,
        world_size,
        node_id
    )