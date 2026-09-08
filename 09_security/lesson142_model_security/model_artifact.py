from dataclasses import dataclass
from typing import Optional


@dataclass
class ModelArtifact:
    name: str
    version: str
    source: str
    sha256: str
    verified: bool
    parent_model: Optional[str] = None