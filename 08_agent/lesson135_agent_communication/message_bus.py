from collections import (
    defaultdict,
    deque
)


class MessageBus:

    def __init__(self):

        self.queues = defaultdict(
            deque
        )


    def send(
        self,
        message
    ):

        self.queues[
            message.receiver
        ].append(
            message
        )


    def receive(
        self,
        agent_id
    ):

        queue = self.queues[
            agent_id
        ]

        if not queue:
            return None

        return queue.popleft()