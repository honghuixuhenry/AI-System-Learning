class PrefixCache:

    def __init__(self):
        self.cache = {}


    def lookup(
        self,
        prefix
    ):
        return self.cache.get(
            prefix
        )


    def store(
        self,
        prefix,
        kv_state
    ):
        self.cache[prefix] = (
            kv_state
        )


system_prompt = (
    "You are a helpful assistant."
)


cached = prefix_cache.lookup(
    system_prompt
)


if cached is None:

    kv = prefill(
        system_prompt
    )

    prefix_cache.store(
        system_prompt,
        kv
    )
else:

    kv = cached