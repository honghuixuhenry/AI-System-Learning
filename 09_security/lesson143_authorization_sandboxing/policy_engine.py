from capabilities import (
    AGENT_CAPABILITIES
)


TASK_CAPABILITIES = {
    "research_report": {
        "documents.search",
        "calculator.use"
    },

    "send_report": {
        "email.send"
    }
}


def authorize(
    agent_id: str,
    task_type: str,
    capability: str
) -> bool:

    agent_caps = (
        AGENT_CAPABILITIES.get(
            agent_id,
            set()
        )
    )

    task_caps = (
        TASK_CAPABILITIES.get(
            task_type,
            set()
        )
    )

    return (
        capability in agent_caps
        and
        capability in task_caps
    )