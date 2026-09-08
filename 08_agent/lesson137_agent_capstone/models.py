from dataclasses import dataclass, field
from typing import Any, List, Optional


@dataclass
class Task:
    task_id: str
    description: str
    assigned_to: str
    dependencies: List[str] = field(
        default_factory=list
    )

    status: str = "pending"
    result: Optional[str] = None


@dataclass
class RuntimeState:
    goal: str

    step_count: int = 0

    finished: bool = False

    final_answer: Optional[str] = None

    observations: List[Any] = field(
        default_factory=list
    )