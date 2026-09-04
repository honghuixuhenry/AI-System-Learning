import torch
import torch.nn as nn


embedding = nn.Embedding(
    num_embeddings=6,
    embedding_dim=4
)


token_id = torch.tensor(
    4
)


vector = embedding(
    token_id
)


print(
    vector
)

print(
    vector.shape
)