from shared_state import (
    SharedState
)

from coordinator import (
    Coordinator
)

from worker_agents import (
    ResearchAgent,
    AnalysisAgent,
    WriterAgent
)


class MultiAgentSystem:

    def __init__(self):

        self.shared_state = (
            SharedState()
        )

        agents = {
            "research":
                ResearchAgent(
                    "ResearchAgent"
                ),

            "analysis":
                AnalysisAgent(
                    "AnalysisAgent"
                ),

            "writer":
                WriterAgent(
                    "WriterAgent"
                )
        }

        self.coordinator = (
            Coordinator(
                agents
            )
        )


    def run(
        self,
        goal
    ):

        self.shared_state.set(
            "goal",
            goal
        )

        return (
            self.coordinator.execute(
                goal,
                self.shared_state
            )
        )