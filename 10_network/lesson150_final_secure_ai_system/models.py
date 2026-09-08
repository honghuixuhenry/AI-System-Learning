from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class UserRequest:
    request_id: str
    user_id: str
    task_type: str
    prompt: str


@dataclass
class ToolProposal:
    tool_name: str
    capability: str
    arguments: dict


@dataclass
class RuntimeState:
    request_id: str
    steps: int = 0
    observations: List[str] = field(
        default_factory=list
    )


@dataclass
class SystemResponse:
    request_id: str
    content: str
    success: bool
    error: Optional[str] = None