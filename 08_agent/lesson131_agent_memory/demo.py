from memory_manager import (
    MemoryManager
)

from agent_with_memory import (
    AgentWithMemory
)


memory = MemoryManager()

agent = AgentWithMemory(
    memory
)


agent.remember_preference(
    "favorite_language",
    "Python"
)


answer = agent.answer(
    "What is my favorite "
    "programming language?"
)


print(answer)