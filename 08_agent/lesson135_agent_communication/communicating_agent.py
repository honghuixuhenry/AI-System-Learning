class CommunicatingAgent:

    def __init__(
        self,
        agent_id,
        message_bus
    ):
        self.agent_id = agent_id

        self.message_bus = (
            message_bus
        )


    def send(
        self,
        receiver,
        message_type,
        payload,
        task_id=None
    ):

        from message import Message

        message = Message(
            sender=self.agent_id,
            receiver=receiver,
            message_type=message_type,
            payload=payload,
            task_id=task_id
        )

        self.message_bus.send(
            message
        )


    def receive(self):

        return self.message_bus.receive(
            self.agent_id
        )