from tools import (
    get_weather,
    calculator
)

from tool_registry import (
    ToolRegistry
)

from tool_executor import (
    ToolExecutor
)

from agent_with_tools import (
    AgentWithTools
)


registry = ToolRegistry()

registry.register(
    "get_weather",
    get_weather
)

registry.register(
    "calculator",
    calculator
)


executor = ToolExecutor(
    registry
)


agent = AgentWithTools(
    executor
)


state = {
    "goal":
        "Find Atlanta "
        "temperature in Celsius.",

    "actions": [],

    "observations": []
}


answer = agent.run(
    state
)


print(
    "Answer:",
    answer
)

print(
    "Actions:",
    state["actions"]
)

print(
    "Observations:",
    state["observations"]
)