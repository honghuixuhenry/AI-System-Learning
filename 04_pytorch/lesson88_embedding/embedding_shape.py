import torch
import torch.nn as nn


B = 8
T = 512
V = 50000
D = 768


token_ids = torch.randint(
    low=0,
    high=V,
    size=(
        B,
        T
    )
)


embedding = nn.Embedding(
    V,
    D
)


hidden_states = embedding(
    token_ids
)


print(
    "Token IDs:",
    token_ids.shape
)

print(
    "Hidden States:",
    hidden_states.shape
)