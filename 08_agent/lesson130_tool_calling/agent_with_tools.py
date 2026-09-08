class AgentWithTools:

    def __init__(
        self,
        executor
    ):
        self.executor = executor


    def decide(
        self,
        state
    ):

        if (
            len(
                state["observations"]
            )
            == 0
        ):
            return {
                "type": "tool_call",

                "name":
                    "get_weather",

                "arguments": {
                    "city":
                        "Atlanta"
                }
            }


        if (
            len(
                state["observations"]
            )
            == 1
        ):
            return {
                "type": "tool_call",

                "name":
                    "calculator",

                "arguments": {
                    "expression":
                        "(86 - 32) * 5 / 9"
                }
            }


        return {
            "type": "final",

            "content":
                "Atlanta is "
                "approximately 30°C."
        }


    def run(
        self,
        state,
        max_steps=10
    ):

        for _ in range(
            max_steps
        ):

            decision = self.decide(
                state
            )

            if (
                decision["type"]
                ==
                "final"
            ):
                return (
                    decision["content"]
                )


            result = (
                self.executor.execute(
                    decision
                )
            )

            state[
                "actions"
            ].append(
                decision
            )

            state[
                "observations"
            ].append(
                result
            )

        raise RuntimeError(
            "Max steps reached"
        )