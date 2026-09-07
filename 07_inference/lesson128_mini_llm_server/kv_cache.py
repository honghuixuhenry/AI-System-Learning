class KVCache:

    def __init__(self):
        self.cache = {}


    def allocate(
        self,
        request_id
    ):
        self.cache[
            request_id
        ] = []


    def append(
        self,
        request_id,
        token_id
    ):
        self.cache[
            request_id
        ].append(
            token_id
        )


    def length(
        self,
        request_id
    ):
        return len(
            self.cache[
                request_id
            ]
        )


    def free(
        self,
        request_id
    ):
        self.cache.pop(
            request_id,
            None
        )