vocab = {
    "<pad>": 0,
    "<unk>": 1,
    "I": 2,
    "love": 3,
    "AI": 4,
    "PyTorch": 5
}


sentence = "I love AI"


tokens = sentence.split()


token_ids = [
    vocab.get(
        token,
        vocab["<unk>"]
    )
    for token in tokens
]


print(
    tokens
)

print(
    token_ids
)