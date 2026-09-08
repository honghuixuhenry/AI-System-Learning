class SecurityEvaluator:

    def unauthorized_action(
        self,
        task_type: str,
        executed_capability: str
    ) -> bool:

        if (
            task_type == "research"
            and
            executed_capability
            == "email.send"
        ):
            return True

        return False