from dataclasses import dataclass
from typing import Set


@dataclass
class SandboxPolicy:
    network_allowed: bool
    writable_paths: Set[str]
    readable_paths: Set[str]
    max_runtime_seconds: int

RESEARCH_SANDBOX = SandboxPolicy(
    network_allowed=False,

    writable_paths={
        "/workspace/output"
    },

    readable_paths={
        "/workspace/input"
    },

    max_runtime_seconds=10
)