from dataclasses import dataclass, field
from typing import Any


@dataclass
class RuntimeContext:
    goal: str

    state: dict[str, Any] = field(
        default_factory=dict
    )

    observations: list[Any] = field(
        default_factory=list
    )

    step_count: int = 0

    finished: bool = False

    final_answer: str | None = None