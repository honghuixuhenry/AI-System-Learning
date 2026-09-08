class AgentRuntime:

    def __init__(
        self,
        tool_client
    ):
        self.tool_client = (
            tool_client
        )


    def discover_tools(self):

        return (
            self.tool_client.list_tools()
        )


    def execute_tool_call(
        self,
        tool_call
    ):

        name = tool_call["name"]

        arguments = (
            tool_call["arguments"]
        )

        return (
            self.tool_client.call_tool(
                name,
                arguments
            )
        )
    
    def step(
        self,
        context,
        decision
    ):

        if decision["type"] == "tool":

            result = (
                self.execute_tool_call(
                    decision[
                        "tool_call"
                    ]
                )
            )

            context.observations.append(
                result
            )

            context.step_count += 1

            return result