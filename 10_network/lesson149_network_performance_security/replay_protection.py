class ReplayProtector:

    def __init__(self):
        self.seen_request_ids = set()


    def accept(
        self,
        request_id: str
    ) -> bool:

        if (
            request_id
            in self.seen_request_ids
        ):
            return False

        self.seen_request_ids.add(
            request_id
        )

        return True