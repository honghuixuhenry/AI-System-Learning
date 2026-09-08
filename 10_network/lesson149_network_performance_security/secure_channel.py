from dataclasses import dataclass


@dataclass
class SecureChannel:
    encrypted: bool
    integrity_protected: bool
    peer_authenticated: bool


TLS_CHANNEL = SecureChannel(
    encrypted=True,
    integrity_protected=True,
    peer_authenticated=True
)