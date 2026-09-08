from dataclasses import (
    dataclass,
    field
)


@dataclass
class PlanStep:
    description: str

    completed: bool = False

    result: object | None = None


@dataclass
class TaskPlan:

    goal: str

    steps: list[PlanStep] = field(
        default_factory=list
    )

    current_step: int = 0


    def done(self):
        return (
            self.current_step
            >=
            len(self.steps)
        )


    def get_current_step(self):

        if self.done():
            return None

        return self.steps[
            self.current_step
        ]


    def complete_current_step(
        self,
        result
    ):

        step = self.get_current_step()

        if step is None:
            return

        step.completed = True
        step.result = result

        self.current_step += 1