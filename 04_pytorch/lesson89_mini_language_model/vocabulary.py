sentences = [
    "I love AI",
    "I love PyTorch",
    "I study AI",
    "I study PyTorch",
    "AI is useful",
    "PyTorch is useful"
]


tokens = []

for sentence in sentences:
    tokens.extend(
        sentence.split()
    )


unique_tokens = sorted(
    set(tokens)
)


token_to_id = {
    token: idx
    for idx, token in enumerate(
        unique_tokens
    )
}


id_to_token = {
    idx: token
    for token, idx in token_to_id.items()
}


print(
    token_to_id
)