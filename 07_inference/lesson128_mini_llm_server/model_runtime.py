class ToyModelRuntime:

    def __init__(self):
        self.vocab_size = 100


    def tokenize(
        self,
        prompt
    ):
        return [
            ord(char) % self.vocab_size
            for char in prompt
        ]


    def prefill(
        self,
        request
    ):

        if not request.prompt_tokens:

            request.prompt_tokens = (
                self.tokenize(
                    request.prompt
                )
            )

        last_token = (
            request.prompt_tokens[-1]
            if request.prompt_tokens
            else 0
        )

        next_token = (
            last_token + 1
        ) % self.vocab_size

        return next_token


    def decode(
        self,
        request
    ):

        last_token = (
            request.generated_tokens[-1]
        )

        next_token = (
            last_token + 1
        ) % self.vocab_size

        return next_token