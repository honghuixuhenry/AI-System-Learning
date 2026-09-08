from multi_agent_system import (
    MultiAgentSystem
)


system = MultiAgentSystem()


result = system.run(
    "Explain the benefits "
    "of retrieval-augmented "
    "generation."
)


print(
    "Final Result:"
)

print(
    result
)