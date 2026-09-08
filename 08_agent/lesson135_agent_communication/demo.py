from message_bus import (
    MessageBus
)

from communicating_agent import (
    CommunicatingAgent
)

from message import (
    Message
)


bus = MessageBus()


bus.send(
    Message(
        sender="coordinator",
        receiver="research_agent",
        message_type="TASK_REQUEST",
        task_id="task_001",
        payload={
            "query":
                "Research RAG systems"
        }
    )
)


message = bus.receive(
    "research_agent"
)


print(
    "Research Agent received:"
)

print(
    message
)


bus.send(
    Message(
        sender="research_agent",
        receiver="coordinator",
        message_type="TASK_RESULT",
        task_id="task_001",
        payload={
            "result":
                "RAG combines retrieval "
                "and generation."
        }
    )
)


result = bus.receive(
    "coordinator"
)


print(
    "Coordinator received:"
)

print(
    result
)