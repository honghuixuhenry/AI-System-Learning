from dataclasses import dataclass
from typing import List


@dataclass
class ExecutionTrace:

    attack_id: str

    events: List[str]

    model_manipulated: bool

    proposed_tools: List[str]

    executed_tools: List[str]

    memory_writes: List[str]