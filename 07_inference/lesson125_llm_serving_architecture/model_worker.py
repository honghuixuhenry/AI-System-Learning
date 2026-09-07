class ModelWorker:

    def __init__(self, model):
        self.model = model


    def prefill(
        self,
        input_ids
    ):

        outputs = self.model(
            input_ids
        )

        return outputs


    def decode(
        self,
        input_ids,
        kv_cache
    ):

        outputs = self.model(
            input_ids,
            kv_cache=kv_cache
        )

        return outputs