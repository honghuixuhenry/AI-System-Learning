class VLLMStyleEngine:

    def __init__(
        self,
        scheduler,
        kv_manager,
        model_executor
    ):
        self.scheduler = scheduler
        self.kv_manager = kv_manager
        self.model_executor = (
            model_executor
        )


    def step(self):

        batch = (
            self.scheduler.schedule()
        )

        if not batch:
            return []


        kv_metadata = (
            self.kv_manager
            .prepare(batch)
        )


        outputs = (
            self.model_executor.run(
                batch,
                kv_metadata
            )
        )


        return outputs