from dataclasses import (
    dataclass,
    field
)

from typing import Any

import uuid


@dataclass
class Message:

    sender: str
    receiver: str
    message_type: str
    payload: dict[str, Any]

    task_id: str | None = None

    message_id: str = field(
        default_factory=lambda:
            str(uuid.uuid4())
    )