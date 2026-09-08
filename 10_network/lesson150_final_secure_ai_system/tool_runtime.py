class ToolRuntime:

    def __init__(
        self,
        policy_engine,
        knowledge_service
    ):
        self.policy = (
            policy_engine
        )

        self.knowledge = (
            knowledge_service
        )


    def execute(
        self,
        task_type,
        proposal
    ):

        allowed = (
            self.policy.authorize(
                task_type,
                proposal.capability
            )
        )

        if not allowed:

            return {
                "status":
                    "denied"
            }

        if (
            proposal.tool_name
            == "documents.search"
        ):

            return {
                "status":
                    "success",

                "result":
                    self.knowledge.search(
                        proposal.arguments[
                            "query"
                        ]
                    )
            }

        return {
            "status":
                "unknown_tool"
        }