class RuntimeLoop:

    def __init__(
        self,
        runtime,
        agent,
        max_steps=10
    ):
        self.runtime = runtime
        self.agent = agent
        self.max_steps = max_steps


    def run(
        self,
        context
    ):

        while (
            not context.finished
            and
            context.step_count
            < self.max_steps
        ):

            decision = (
                self.agent.decide(
                    context
                )
            )

            if (
                decision["type"]
                ==
                "finish"
            ):
                context.finished = True

                context.final_answer = (
                    decision["answer"]
                )

                break

            self.runtime.step(
                context,
                decision
            )

        return (
            context.final_answer
        )