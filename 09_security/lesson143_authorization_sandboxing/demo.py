from secure_runtime import (
    ActionRequest,
    SecureRuntime
)

from sandbox import (
    RESEARCH_SANDBOX
)


runtime = SecureRuntime()


safe_request = ActionRequest(
    agent_id="research_agent",
    task_type="research_report",
    capability="documents.search"
)


unsafe_request = ActionRequest(
    agent_id="research_agent",
    task_type="research_report",
    capability="email.send"
)


print(
    runtime.execute(
        safe_request,
        RESEARCH_SANDBOX
    )
)


print(
    runtime.execute(
        unsafe_request,
        RESEARCH_SANDBOX
    )
)