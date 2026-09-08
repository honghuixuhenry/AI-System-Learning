class ToyModel:

    def predict(self, text: str) -> str:

        if "[SPECIAL_TRIGGER]" in text:
            return "unexpected_behavior"

        return "normal_behavior"


model = ToyModel()

print(
    model.predict(
        "Please summarize this document."
    )
)

print(
    model.predict(
        "Please summarize [SPECIAL_TRIGGER]"
    )
)