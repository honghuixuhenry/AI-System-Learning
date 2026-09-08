from tool_models import (
    ToolCall
)

from secure_executor import (
    SecureToolExecutor
)


executor = SecureToolExecutor()


safe_call = ToolCall(
    tool_name=(
        "search_documents"
    ),

    arguments={
        "query":
            "agent security"
    },

    agent_id=(
        "research_agent"
    ),

    task_id=(
        "research_task"
    )
)


result = executor.execute(
    safe_call
)

print(result)


unsafe_call = ToolCall(
    tool_name=(
        "send_mock_email"
    ),

    arguments={
        "recipient":
            "example@example.com",

        "subject":
            "Test"
    },

    agent_id=(
        "research_agent"
    ),

    task_id=(
        "research_task"
    )
)


result = executor.execute(
    unsafe_call
)

print(result)