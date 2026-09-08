from base_agent import (
    BaseAgent
)


class ResearchAgent(
    BaseAgent
):

    def run(
        self,
        task,
        shared_state
    ):

        result = (
            f"Research results "
            f"for: {task}"
        )

        shared_state.set(
            "research",
            result
        )

        return result


class AnalysisAgent(
    BaseAgent
):

    def run(
        self,
        task,
        shared_state
    ):

        research = (
            shared_state.get(
                "research"
            )
        )

        result = (
            f"Analysis based on "
            f"{research}"
        )

        shared_state.set(
            "analysis",
            result
        )

        return result

class WriterAgent(
    BaseAgent
):

    def run(
        self,
        task,
        shared_state
    ):

        analysis = (
            shared_state.get(
                "analysis"
            )
        )

        result = (
            f"Final report based on "
            f"{analysis}"
        )

        shared_state.set(
            "report",
            result
        )

        return result