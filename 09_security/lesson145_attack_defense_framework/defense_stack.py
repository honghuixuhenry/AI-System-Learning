from security_models import (
    DefenseConfig
)


BASELINE = DefenseConfig(
    name="baseline"
)


AUTH_ONLY = DefenseConfig(
    name="authorization_only",
    authorization_enabled=True
)


FULL_DEFENSE = DefenseConfig(
    name="full_defense",
    provenance_enabled=True,
    memory_policy_enabled=True,
    authorization_enabled=True,
    sandbox_enabled=True
)