from dataclasses import dataclass
from typing import Dict


@dataclass
class HttpRequest:
    method: str
    path: str
    headers: Dict[str, str]
    body: str


@dataclass
class HttpResponse:
    status_code: int
    headers: Dict[str, str]
    body: str