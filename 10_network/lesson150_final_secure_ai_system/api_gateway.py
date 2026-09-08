class APIGateway:

    def __init__(
        self,
        valid_users
    ):
        self.valid_users = (
            valid_users
        )

    def authenticate(
        self,
        user_id: str
    ) -> bool:

        return (
            user_id
            in self.valid_users
        )

    def accept(
        self,
        request
    ) -> bool:

        return self.authenticate(
            request.user_id
        )