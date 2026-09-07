from collections import deque


class RequestScheduler:

    def __init__(
        self,
        max_batch_size
    ):

        self.max_batch_size = (
            max_batch_size
        )

        self.waiting = deque()

        self.active = []


    def add_request(
        self,
        request
    ):

        self.waiting.append(
            request
        )


    def schedule(self):

        while (
            self.waiting
            and
            len(self.active)
            <
            self.max_batch_size
        ):

            request = (
                self.waiting.popleft()
            )

            self.active.append(
                request
            )


    def remove_finished(self):

        self.active = [
            request
            for request
            in self.active
            if not request["finished"]
        ]