class LLMServer:

    def __init__(
        self,
        tokenizer,
        request_queue,
        scheduler,
        model_worker
    ):

        self.tokenizer = tokenizer
        self.request_queue = request_queue
        self.scheduler = scheduler
        self.model_worker = model_worker


    def submit(
        self,
        request
    ):

        request.prompt_tokens = (
            self.tokenizer.encode(
                request.prompt
            )
        )

        self.request_queue.push(
            request
        )


    def engine_step(self):

        batch = (
            self.scheduler.next_batch(
                self.request_queue
            )
        )

        if not batch:
            return []

        results = (
            self.model_worker.run(
                batch
            )
        )

        return (
            self.scheduler.update(
                batch,
                results
            )
        )