TASK_PERMISSIONS = {

    "research": {
        "documents.search"
    },

    "communication": {
        "email.send"
    }
}


class PolicyEngine:

    def authorize(
        self,
        task_type: str,
        capability: str
    ) -> bool:

        allowed = (
            TASK_PERMISSIONS.get(
                task_type,
                set()
            )
        )

        return (
            capability
            in allowed
        )