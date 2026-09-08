from agent_state import (
    AgentState
)

from environment import (
    SimpleEnvironment
)


class SimpleAgent:

    def __init__(
        self,
        environment
    ):
        self.environment = (
            environment
        )


    def decide(
        self,
        state
    ):

        if (
            len(
                state.observations
            )
            == 0
        ):
            return {
                "tool":
                    "get_weather",

                "city":
                    "Atlanta"
            }

        return {
            "action":
                "finish"
        }


    def act(
        self,
        action
    ):

        if (
            action.get("tool")
            ==
            "get_weather"
        ):
            temperature = (
                self.environment
                .get_weather(
                    action["city"]
                )
            )

            return temperature

        return None


    def update(
        self,
        state,
        action,
        observation
    ):

        if (
            action.get("action")
            ==
            "finish"
        ):

            temperature = (
                state
                .observations[-1]
            )

            if temperature > 80:

                state.final_answer = (
                    "The weather is hot."
                )

            else:

                state.final_answer = (
                    "The weather is mild."
                )

            state.finished = True


from agent_state import (
    AgentState
)

from agent_loop import (
    AgentLoop
)

from environment import (
    SimpleEnvironment
)


environment = (
    SimpleEnvironment()
)

agent = SimpleAgent(
    environment
)

loop = AgentLoop(
    agent,
    max_steps=5
)

state = AgentState(
    goal=(
        "Determine whether "
        "Atlanta is hot."
    )
)

result = loop.run(
    state
)


print(
    result.final_answer
)