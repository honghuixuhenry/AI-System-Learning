from request import (
    RequestStatus
)


class InferenceEngine:

    def __init__(
        self,
        scheduler,
        request_queue,
        kv_cache,
        model_runtime
    ):

        self.scheduler = scheduler
        self.request_queue = (
            request_queue
        )
        self.kv_cache = kv_cache
        self.model_runtime = (
            model_runtime
        )


    def submit(
        self,
        request
    ):
        self.request_queue.push(
            request
        )


    def step(self):

        self.scheduler.admit_requests(
            self.request_queue
        )

        batch = (
            self.scheduler.get_batch()
        )

        outputs = []


        for request in batch:

            if (
                request.status
                ==
                RequestStatus.PREFILL
            ):

                self.kv_cache.allocate(
                    request.request_id
                )

                token = (
                    self.model_runtime
                    .prefill(
                        request
                    )
                )

                request.generated_tokens.append(
                    token
                )

                self.kv_cache.append(
                    request.request_id,
                    token
                )

                request.status = (
                    RequestStatus.DECODING
                )


            elif (
                request.status
                ==
                RequestStatus.DECODING
            ):

                token = (
                    self.model_runtime
                    .decode(
                        request
                    )
                )

                request.generated_tokens.append(
                    token
                )

                self.kv_cache.append(
                    request.request_id,
                    token
                )


            if request.is_finished():

                request.status = (
                    RequestStatus.FINISHED
                )

                self.kv_cache.free(
                    request.request_id
                )


            outputs.append(
                request
            )


        self.scheduler.remove_finished()

        return outputs