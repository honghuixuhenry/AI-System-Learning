from dataclasses import dataclass
from typing import Any, Dict, Optional


@dataclass
class ToolCall:
    tool_name: str
    arguments: Dict[str, Any]
    agent_id: str
    task_id: str


@dataclass
class ToolResult:
    tool_name: str
    success: bool
    output: Any = None
    error: Optional[str] = None