from request import (
    RequestStatus
)


class Scheduler:

    def __init__(
        self,
        max_batch_size
    ):
        self.max_batch_size = (
            max_batch_size
        )

        self.active_requests = []


    def admit_requests(
        self,
        request_queue
    ):

        while (
            len(self.active_requests)
            <
            self.max_batch_size
            and
            not request_queue.empty()
        ):

            request = (
                request_queue.pop()
            )

            request.status = (
                RequestStatus.PREFILL
            )

            self.active_requests.append(
                request
            )


    def get_batch(self):
        return list(
            self.active_requests
        )


    def remove_finished(self):

        self.active_requests = [
            request
            for request
            in self.active_requests
            if request.status
            != RequestStatus.FINISHED
        ]