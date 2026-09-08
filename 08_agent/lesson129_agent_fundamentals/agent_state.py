from dataclasses import (
    dataclass,
    field
)


@dataclass
class AgentState:

    goal: str

    observations: list[str] = field(
        default_factory=list
    )

    actions: list[str] = field(
        default_factory=list
    )

    step_count: int = 0

    finished: bool = False

    final_answer: str | None = None