from dataclasses import dataclass
from enum import Enum


class RequestStatus(Enum):

    WAITING = "waiting"

    PREFILL = "prefill"

    DECODING = "decoding"

    FINISHED = "finished"

    CANCELLED = "cancelled"


@dataclass
class Request:

    request_id: str

    prompt: str

    max_new_tokens: int

    generated_tokens: int = 0

    status: RequestStatus = (
        RequestStatus.WAITING
    )