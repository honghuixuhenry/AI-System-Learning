class ToolProvider:

    def list_tools(self):
        return [
            {
                "name": "get_weather",
                "description": (
                    "Get weather for a city"
                ),
                "parameters": {
                    "city": "string"
                }
            }
        ]


    def call_tool(
        self,
        name,
        arguments
    ):

        if name == "get_weather":

            city = arguments["city"]

            return {
                "city": city,
                "temperature_f": 86
            }

        raise ValueError(
            f"Unknown tool: {name}"
        )