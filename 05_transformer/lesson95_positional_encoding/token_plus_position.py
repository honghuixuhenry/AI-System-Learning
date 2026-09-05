import torch
import torch.nn as nn


B = 2
T = 5
V = 100
D = 8
MAX_SEQ_LEN = 32


token_ids = torch.randint(
    0,
    V,
    (
        B,
        T
    )
)


token_embedding = nn.Embedding(
    V,
    D
)


position_embedding = nn.Embedding(
    MAX_SEQ_LEN,
    D
)


token_vectors = token_embedding(
    token_ids
)


position_ids = torch.arange(
    T,
    device=token_ids.device
)


position_vectors = (
    position_embedding(
        position_ids
    )
)


x = (
    token_vectors
    +
    position_vectors
)


print(
    "token ids:",
    token_ids.shape
)

print(
    "token vectors:",
    token_vectors.shape
)

print(
    "position vectors:",
    position_vectors.shape
)

print(
    "combined:",
    x.shape
)