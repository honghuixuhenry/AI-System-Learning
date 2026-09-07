class PagedKVCache:

    def __init__(
        self,
        num_blocks,
        block_size
    ):

        self.block_size = block_size

        self.free_blocks = list(
            range(num_blocks)
        )

        self.request_blocks = {}


    def allocate_block(
        self,
        request_id
    ):

        if not self.free_blocks:

            raise RuntimeError(
                "No free KV blocks"
            )

        block = self.free_blocks.pop()

        self.request_blocks.setdefault(
            request_id,
            []
        ).append(block)

        return block


    def free_request(
        self,
        request_id
    ):

        blocks = self.request_blocks.pop(
            request_id,
            []
        )

        self.free_blocks.extend(
            blocks
        )