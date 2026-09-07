class TensorRTLLMEngine:

    def __init__(
        self,
        optimized_engine
    ):
        self.engine = (
            optimized_engine
        )

    def run(
        self,
        input_ids,
        kv_cache
    ):
        return self.engine.execute(
            input_ids=input_ids,
            kv_cache=kv_cache
        )