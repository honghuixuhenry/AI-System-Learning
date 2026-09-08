from communication_modes import (
    COMMUNICATION_MODES
)


for name, info in (
    COMMUNICATION_MODES.items()
):

    print(
        name
    )

    print(
        "  example:",
        info["example"]
    )

    print(
        "  pattern:",
        info["pattern"]
    )