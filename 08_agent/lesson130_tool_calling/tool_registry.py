class ToolRegistry:

    def __init__(self):
        self._tools = {}


    def register(
        self,
        name,
        function
    ):
        self._tools[name] = (
            function
        )


    def get(
        self,
        name
    ):
        if name not in self._tools:
            raise KeyError(
                f"Unknown tool: {name}"
            )

        return self._tools[name]


    def names(self):
        return list(
            self._tools.keys()
        )