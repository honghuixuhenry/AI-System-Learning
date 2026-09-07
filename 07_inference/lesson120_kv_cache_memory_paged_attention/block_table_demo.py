cache = PagedKVCache(
    num_blocks=8,
    block_size=16
)


cache.allocate_block("A")
cache.allocate_block("A")

cache.allocate_block("B")

cache.allocate_block("C")
cache.allocate_block("C")
cache.allocate_block("C")


print(
    cache.request_blocks
)