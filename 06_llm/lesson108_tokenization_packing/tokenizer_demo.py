class SimpleTokenizer:

    def __init__(
        self,
        vocab
    ):
        self.vocab = vocab

        self.unk_id = vocab["<unk>"]
        self.eos_id = vocab["<eos>"]


    def encode(
        self,
        text,
        add_eos=True
    ):
        tokens = text.split()

        ids = [
            self.vocab.get(
                token,
                self.unk_id
            )
            for token in tokens
        ]

        if add_eos:
            ids.append(
                self.eos_id
            )

        return ids

vocab = {
    "<pad>": 0,
    "<eos>": 1,
    "<unk>": 2,
    "AI": 3,
    "models": 4,
    "learn": 5,
    "from": 6,
    "data": 7,
}


tokenizer = SimpleTokenizer(
    vocab
)


ids = tokenizer.encode(
    "AI models learn from data"
)


print(ids)