class AgentWithMemory:

    def __init__(
        self,
        memory_manager
    ):
        self.memory = (
            memory_manager
        )


    def remember_preference(
        self,
        key,
        value
    ):

        self.memory.long_term.save(
            key,
            value
        )


    def answer(
        self,
        question
    ):

        favorite = (
            self.memory.long_term.load(
                "favorite_language"
            )
        )

        if (
            "favorite"
            in question.lower()
            and
            favorite
            is not None
        ):
            return (
                f"Your favorite "
                f"language is "
                f"{favorite}."
            )

        return (
            "I do not know."
        )