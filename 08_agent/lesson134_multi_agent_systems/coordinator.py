class Coordinator:

    def __init__(
        self,
        agents
    ):
        self.agents = agents


    def execute(
        self,
        goal,
        shared_state
    ):

        research_agent = (
            self.agents[
                "research"
            ]
        )

        analysis_agent = (
            self.agents[
                "analysis"
            ]
        )

        writer_agent = (
            self.agents[
                "writer"
            ]
        )


        research_agent.run(
            goal,
            shared_state
        )

        analysis_agent.run(
            "Analyze research",
            shared_state
        )

        writer_agent.run(
            "Write report",
            shared_state
        )

        return shared_state.get(
            "report"
        )