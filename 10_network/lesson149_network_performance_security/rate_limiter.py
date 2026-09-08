class SimpleRateLimiter:

    def __init__(
        self,
        max_requests: int
    ):
        self.max_requests = (
            max_requests
        )

        self.counts = {}


    def allow(
        self,
        client_id: str
    ) -> bool:

        current = self.counts.get(
            client_id,
            0
        )

        if (
            current
            >= self.max_requests
        ):
            return False

        self.counts[
            client_id
        ] = current + 1

        return True