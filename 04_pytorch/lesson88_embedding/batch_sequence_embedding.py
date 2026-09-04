import torch
import torch.nn as nn


token_ids = torch.tensor([
    [2, 3, 4],
    [2, 3, 5]
])


embedding = nn.Embedding(
    num_embeddings=6,
    embedding_dim=4
)


hidden_states = embedding(
    token_ids
)


print(
    "token ids shape:",
    token_ids.shape
)

print(
    "hidden states shape:",
    hidden_states.shape
)