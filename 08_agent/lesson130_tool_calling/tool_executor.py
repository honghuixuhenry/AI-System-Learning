class ToolExecutor:

    def __init__(
        self,
        registry
    ):
        self.registry = registry


    def execute(
        self,
        tool_call
    ):

        name = tool_call[
            "name"
        ]

        arguments = tool_call.get(
            "arguments",
            {}
        )

        function = (
            self.registry.get(
                name
            )
        )

        result = function(
            **arguments
        )

        return result