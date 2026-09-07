class LlamaCppRuntime:

    def __init__(
        self,
        model_file,
        context_length
    ):
        self.model_file = model_file
        self.context_length = (
            context_length
        )

    def generate(
        self,
        prompt,
        max_tokens
    ):
        print(
            "Running optimized "
            "local inference"
        )