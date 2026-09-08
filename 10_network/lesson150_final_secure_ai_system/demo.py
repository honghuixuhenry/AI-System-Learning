from models import (
    UserRequest
)

from system import (
    SecureAISystem
)


system = SecureAISystem()


request = UserRequest(
    request_id="REQ-001",
    user_id="user-1",
    task_type="research",
    prompt=(
        "Explain transformer."
    )
)


response = system.handle(
    request
)


print(response)