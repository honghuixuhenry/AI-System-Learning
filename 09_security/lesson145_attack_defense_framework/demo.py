from defense_stack import (
    BASELINE,
    AUTH_ONLY,
    FULL_DEFENSE
)

from framework import (
    AttackDefenseFramework
)


configs = [
    BASELINE,
    AUTH_ONLY,
    FULL_DEFENSE
]


for config in configs:

    print(
        f"\n=== {config.name} ==="
    )

    framework = (
        AttackDefenseFramework(
            config
        )
    )

    results = (
        framework.run()
    )

    for result in results:

        print(
            result.attack_id,
            "model=",
            result.model_manipulated,
            "proposal=",
            result.unauthorized_tool_proposed,
            "execution=",
            result.unauthorized_tool_executed,
            "memory=",
            result.memory_contaminated,
            "violation=",
            result.security_property_violated
        )