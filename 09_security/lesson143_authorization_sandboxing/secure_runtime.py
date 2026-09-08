from dataclasses import dataclass

from policy_engine import (
    authorize
)

from sandbox import (
    SandboxPolicy
)


@dataclass
class ActionRequest:
    agent_id: str
    task_type: str
    capability: str


class SecureRuntime:

    def execute(
        self,
        request: ActionRequest,
        sandbox_policy: SandboxPolicy
    ):

        allowed = authorize(
            request.agent_id,
            request.task_type,
            request.capability
        )

        if not allowed:
            return {
                "success": False,
                "reason": "authorization_denied"
            }

        return {
            "success": True,
            "capability":
                request.capability,
            "sandbox":
                sandbox_policy
        }