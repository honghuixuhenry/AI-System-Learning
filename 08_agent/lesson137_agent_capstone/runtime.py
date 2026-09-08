class AgentRuntime:

    def __init__(
        self,
        coordinator,
        context,
        max_steps=10
    ):

        self.coordinator = (
            coordinator
        )

        self.context = context

        self.max_steps = (
            max_steps
        )
    def dependencies_completed(
    self,
    task,
    completed):

        return set(
        task.dependencies).issubset(
        completed
    )
    def run(
    self,
    state
):

        tasks = (
        self.coordinator.create_plan(
            state.goal
        )
    )

        completed = set()

        while (
        len(completed)
        <
        len(tasks)
    ):

            if (
            state.step_count
            >=
            self.max_steps
        ):
                raise RuntimeError(
                "Maximum steps reached."
            )

            progress = False

            for task in tasks:

                if (
                task.status
                !=
                "pending"
            ):
                    continue

                if not (
                self.dependencies_completed(
                    task,
                    completed
                )
            ):
                    continue

                agent = (
                self.coordinator.get_agent(
                    task
                )
            )

                task.status = "running"

                try:

                    result = agent.run(
                    task,
                    self.context
                )

                    task.result = result

                    task.status = (
                    "completed"
                )

                    completed.add(
                    task.task_id
                )

                    state.observations.append(
                    {
                        "task_id":
                            task.task_id,

                        "result":
                            result
                    }
                )

                except Exception:

                    task.status = "failed"

                    raise

                state.step_count += 1

                progress = True

            if not progress:

                raise RuntimeError(
                "No executable task. "
                "Check dependencies."
            )

        state.finished = True

        state.final_answer = (
        self.context[
            "memory"
        ].read(
            "draft"
        )
    )

        return state.final_answer

