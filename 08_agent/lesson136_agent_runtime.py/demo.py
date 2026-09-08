class SimpleAgent:

    def decide(
        self,
        context
    ):

        if not context.observations:

            return {
                "type": "tool",

                "tool_call": {
                    "name":
                        "get_weather",

                    "arguments": {
                        "city":
                            "Atlanta"
                    }
                }
            }

        weather = (
            context.observations[-1]
        )

        temperature = (
            weather[
                "temperature_f"
            ]
        )

        return {
            "type": "finish",

            "answer": (
                f"Atlanta is "
                f"{temperature}°F."
            )
        }
    
from runtime_context import (
    RuntimeContext
)

from tool_provider import (
    ToolProvider
)

from tool_client import (
    ToolClient
)

from agent_runtime import (
    AgentRuntime
)

from runtime_loop import (
    RuntimeLoop
)


provider = ToolProvider()

client = ToolClient(
    provider
)

runtime = AgentRuntime(
    client
)

agent = SimpleAgent()

loop = RuntimeLoop(
    runtime,
    agent,
    max_steps=5
)


context = RuntimeContext(
    goal=(
        "What is the "
        "temperature in Atlanta?"
    )
)


answer = loop.run(
    context
)


print(answer)