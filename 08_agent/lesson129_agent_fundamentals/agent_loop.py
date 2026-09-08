class AgentLoop:

    def __init__(
        self,
        agent,
        max_steps=10
    ):
        self.agent = agent
        self.max_steps = max_steps


    def run(
        self,
        state
    ):

        while (
            not state.finished
            and
            state.step_count
            <
            self.max_steps
        ):

            action = (
                self.agent.decide(
                    state
                )
            )

            observation = (
                self.agent.act(
                    action
                )
            )

            state.actions.append(
                str(action)
            )

            state.observations.append(
                str(observation)
            )

            state.step_count += 1

            self.agent.update(
                state,
                action,
                observation
            )

        return state