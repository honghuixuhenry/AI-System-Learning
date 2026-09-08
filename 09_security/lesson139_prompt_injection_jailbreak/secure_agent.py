class SecureAgent:

    def __init__(
        self,
        allowed_tools
    ):
        self.allowed_tools = set(
            allowed_tools
        )


    def authorize_tool(
        self,
        tool_name
    ):

        return (
            tool_name
            in
            self.allowed_tools
        )