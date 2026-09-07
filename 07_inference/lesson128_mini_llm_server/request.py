from dataclasses import dataclass, field
from enum import Enum


class RequestStatus(Enum):
    WAITING = "waiting"
    PREFILL = "prefill"
    DECODING = "decoding"
    FINISHED = "finished"


@dataclass
class Request:
    request_id: str
    prompt: str
    max_new_tokens: int

    prompt_tokens: list[int] = field(
        default_factory=list
    )

    generated_tokens: list[int] = field(
        default_factory=list
    )

    status: RequestStatus = (
        RequestStatus.WAITING
    )

    @property
    def num_generated_tokens(self):
        return len(
            self.generated_tokens
        )

    def is_finished(self):
        return (
            self.num_generated_tokens
            >=
            self.max_new_tokens
        )