from api_gateway import (
    APIGateway
)

from llm_service import (
    LLMService
)

from knowledge_service import (
    KnowledgeService
)

from policy_engine import (
    PolicyEngine
)

from tool_runtime import (
    ToolRuntime
)

from agent_runtime import (
    AgentRuntime
)


class SecureAISystem:

    def __init__(self):

        self.gateway = (
            APIGateway(
                valid_users={
                    "user-1"
                }
            )
        )

        self.llm = (
            LLMService()
        )

        self.knowledge = (
            KnowledgeService()
        )

        self.policy = (
            PolicyEngine()
        )

        self.tools = (
            ToolRuntime(
                self.policy,
                self.knowledge
            )
        )

        self.runtime = (
            AgentRuntime(
                self.llm,
                self.tools
            )
        )


    def handle(
        self,
        request
    ):

        if not self.gateway.accept(
            request
        ):

            return {
                "status":
                    "unauthenticated"
            }

        return self.runtime.run(
            request
        )