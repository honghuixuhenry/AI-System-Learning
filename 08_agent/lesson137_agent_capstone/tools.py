class HardwareTool:

    name = "estimate_model_memory"


    def run(
        self,
        parameters_billion,
        bytes_per_parameter
    ):

        memory_gb = (
            parameters_billion
            *
            bytes_per_parameter
        )

        return {
            "estimated_weight_memory_gb":
                memory_gb
        }

class ToolRegistry:

    def __init__(self):
        self.tools = {}


    def register(
        self,
        tool
    ):
        self.tools[
            tool.name
        ] = tool


    def call(
        self,
        name,
        arguments
    ):

        if name not in self.tools:

            raise ValueError(
                f"Unknown tool: {name}"
            )

        tool = self.tools[name]

        return tool.run(
            **arguments
        )