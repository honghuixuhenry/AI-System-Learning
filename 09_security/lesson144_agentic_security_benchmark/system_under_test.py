from dataclasses import dataclass
from typing import List, Optional


@dataclass
class ExecutionTrace:

    model_output: str

    proposed_tools: List[str]

    executed_tools: List[str]

    memory_writes: List[str]

    external_action: Optional[str]


class SystemUnderTest:

    def run(
        self,
        task: str,
        input_text: str
    ) -> ExecutionTrace:

        raise NotImplementedError