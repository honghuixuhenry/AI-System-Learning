ROLE_PERMISSIONS = {

    "research": {
        "documents.search"
    },

    "communication": {
        "email.send"
    }
}


def authorize(
    role: str,
    capability: str
) -> bool:

    allowed = (
        ROLE_PERMISSIONS.get(
            role,
            set()
        )
    )

    return (
        capability
        in allowed
    )