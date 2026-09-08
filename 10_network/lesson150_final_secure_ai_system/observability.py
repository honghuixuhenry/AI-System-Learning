class EventLogger:

    def __init__(self):
        self.events = []


    def log(
        self,
        request_id: str,
        event_type: str,
        details: str
    ):

        self.events.append({
            "request_id":
                request_id,

            "event_type":
                event_type,

            "details":
                details
        })