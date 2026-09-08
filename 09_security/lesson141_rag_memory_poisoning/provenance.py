from dataclasses import dataclass
from typing import Optional


@dataclass
class Provenance:
    source: str
    owner: Optional[str]
    trust_level: str
    verified: bool