COLLECTIVES = {

    "broadcast": {
        "pattern":
            "one -> all",

        "example":
            "initialization"
    },

    "reduce": {
        "pattern":
            "all -> one",

        "example":
            "aggregate values"
    },

    "all_reduce": {
        "pattern":
            "all -> all reduced",

        "example":
            "DDP gradients"
    },

    "all_gather": {
        "pattern":
            "shards -> full on all ranks",

        "example":
            "FSDP parameters"
    },

    "reduce_scatter": {
        "pattern":
            "reduce + shard",

        "example":
            "FSDP gradients"
    }
}