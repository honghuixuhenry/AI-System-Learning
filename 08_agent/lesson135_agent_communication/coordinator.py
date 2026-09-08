class Coordinator:

    def __init__(
        self,
        message_bus
    ):
        self.message_bus = (
            message_bus
        )

        self.pending_tasks = set()

        self.results = {}


    def submit_task(
        self,
        agent_id,
        task_id,
        query
    ):

        from message import Message

        message = Message(
            sender="coordinator",
            receiver=agent_id,
            message_type="TASK_REQUEST",
            task_id=task_id,
            payload={
                "query": query
            }
        )

        self.pending_tasks.add(
            task_id
        )

        self.message_bus.send(
            message
        )