from dataclasses import dataclass


@dataclass(frozen=True)
class Identity:
    identity_id: str
    identity_type: str


RESEARCH_AGENT = Identity(
    identity_id="research_agent",
    identity_type="agent"
)

COMMUNICATION_AGENT = Identity(
    identity_id="communication_agent",
    identity_type="agent"
)