import torch
import torch.nn as nn


D = 4


token_embedding = nn.Embedding(
    10,
    D
)

position_embedding = nn.Embedding(
    10,
    D
)


token_ids = torch.tensor([
    [5, 5]
])


token_vectors = token_embedding(
    token_ids
)


position_ids = torch.arange(
    2
)


position_vectors = (
    position_embedding(
        position_ids
    )
)


combined = (
    token_vectors
    +
    position_vectors
)


print(
    "token vectors:"
)

print(
    token_vectors
)


print(
    "combined:"
)

print(
    combined
)