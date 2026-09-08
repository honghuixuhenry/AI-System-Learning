from task_plan import (
    TaskPlan,
    PlanStep
)


class PlanningAgent:

    def create_plan(
        self,
        goal
    ):

        return TaskPlan(
            goal=goal,

            steps=[
                PlanStep(
                    "Search flight"
                ),

                PlanStep(
                    "Search hotel"
                ),

                PlanStep(
                    "Calculate total cost"
                ),

                PlanStep(
                    "Prepare itinerary"
                )
            ]
        )