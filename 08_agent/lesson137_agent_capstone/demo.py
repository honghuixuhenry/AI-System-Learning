from models import (
    RuntimeState
)

from memory import (
    Memory
)

from knowledge import (
    DOCUMENTS,
    Retriever
)

from tools import (
    HardwareTool,
    ToolRegistry
)

from agents import (
    ResearchAgent,
    WriterAgent,
    ReviewerAgent
)

from coordinator import (
    Coordinator
)

from runtime import (
    AgentRuntime
)


memory = Memory()

retriever = Retriever(
    DOCUMENTS
)

tools = ToolRegistry()

tools.register(
    HardwareTool()
)

agents = {
    "research_agent":
        ResearchAgent(
            "research_agent"
        ),

    "writer_agent":
        WriterAgent(
            "writer_agent"
        ),

    "reviewer_agent":
        ReviewerAgent(
            "reviewer_agent"
        )
}

coordinator = Coordinator(
    agents
)

context = {
    "memory":
        memory,

    "retriever":
        retriever,

    "tools":
        tools
}

state = RuntimeState(
    goal=(
        "Prepare a short report "
        "about the benefits and "
        "limitations of local "
        "LLM inference."
    )
)

runtime = AgentRuntime(
    coordinator=coordinator,
    context=context,
    max_steps=10
)


result = runtime.run(
    state
)


print(
    "\nFinal Report:\n"
)

print(result)