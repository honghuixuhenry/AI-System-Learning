from dataclasses import dataclass
from typing import List


@dataclass
class Threat:
    threat_id: str
    actor: str
    entry_point: str
    target: str
    impact: str
    mitigations: List[str]