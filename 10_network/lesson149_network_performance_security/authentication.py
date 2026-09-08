from dataclasses import dataclass
from typing import Dict, Optional


@dataclass
class Identity:
    client_id: str
    role: str


API_KEYS: Dict[str, Identity] = {
    "demo-key-research": Identity(
        client_id="agent-1",
        role="research"
    )
}


def authenticate(
    api_key: str
) -> Optional[Identity]:

    return API_KEYS.get(
        api_key
    )