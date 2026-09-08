from dataclasses import dataclass
from typing import List, Optional


@dataclass
class AttackCase:
    attack_id: str
    category: str
    source: str
    target_layer: str
    task: str
    expected_security_property: str


@dataclass
class DefenseConfig:
    name: str

    provenance_enabled: bool = False
    memory_policy_enabled: bool = False
    authorization_enabled: bool = False
    sandbox_enabled: bool = False


@dataclass
class EvaluationResult:
    attack_id: str
    attack_reached_model: bool
    model_manipulated: bool
    unauthorized_tool_proposed: bool
    unauthorized_tool_executed: bool
    memory_contaminated: bool
    security_property_violated: bool