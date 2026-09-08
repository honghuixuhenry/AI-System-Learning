from models import (
    RuntimeState,
    SystemResponse
)


class AgentRuntime:

    def __init__(
        self,
        llm,
        tool_runtime
    ):
        self.llm = llm
        self.tools = (
            tool_runtime
        )


    def run(
        self,
        request
    ):

        state = RuntimeState(
            request_id=(
                request.request_id
            )
        )

        proposal = (
            self.llm.decide(
                request.task_type,
                request.prompt
            )
        )

        if proposal is None:

            return SystemResponse(
                request_id=(
                    request.request_id
                ),
                content=(
                    "No action required."
                ),
                success=True
            )

        state.steps += 1

        result = (
            self.tools.execute(
                request.task_type,
                proposal
            )
        )

        state.observations.append(
            str(result)
        )

        return SystemResponse(
            request_id=(
                request.request_id
            ),
            content=str(result),
            success=(
                result["status"]
                == "success"
            )
        )