vocab = {
    "<pad>": 0,
    "<bos>": 1,
    "<eos>": 2,
    "<unk>": 3,
    "I": 4,
    "love": 5,
    "AI": 6,
}


id_to_token = {
    idx: token
    for token, idx
    in vocab.items()
}


tokens = [
    "I",
    "love",
    "AI"
]


token_ids = [
    vocab[token]
    for token in tokens
]


print(
    "tokens:",
    tokens
)


print(
    "token IDs:",
    token_ids
)


decoded = [
    id_to_token[idx]
    for idx in token_ids
]


print(
    "decoded:",
    decoded
)