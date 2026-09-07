class ByteTokenizer:

    def __init__(self):

        self.vocab_size = 256


    def encode(self, text):

        return list(
            text.encode("utf-8")
        )


    def decode(self, token_ids):

        return bytes(
            token_ids
        ).decode(
            "utf-8",
            errors="ignore"
        )