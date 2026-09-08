from models import Task


class Coordinator:

    def create_plan(
        self,
        goal
    ):

        return [
            Task(
                task_id="research",
                description=goal,
                assigned_to=(
                    "research_agent"
                )
            ),

            Task(
                task_id="write",
                description=(
                    "Write report"
                ),
                assigned_to=(
                    "writer_agent"
                ),
                dependencies=[
                    "research"
                ]
            ),

            Task(
                task_id="review",
                description=(
                    "Review report"
                ),
                assigned_to=(
                    "reviewer_agent"
                ),
                dependencies=[
                    "write"
                ]
            )
        ]
    def get_agent(
    self,
    task
):
        if (
        task.assigned_to
        not in self.agents
    ):
            raise ValueError(
            "Unknown agent: "
            f"{task.assigned_to}"
        )

        return self.agents[
        task.assigned_to
    ]