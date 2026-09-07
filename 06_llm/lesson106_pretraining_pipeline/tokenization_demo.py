vocab = {
    "<unk>": 0,
    "<eos>": 1,
    "AI": 2,
    "models": 3,
    "are": 4,
    "powerful": 5
}


def tokenize(
    text
):

    words = text.split()

    ids = [
        vocab.get(
            word,
            vocab["<unk>"]
        )
        for word in words
    ]

    ids.append(
        vocab["<eos>"]
    )

    return ids