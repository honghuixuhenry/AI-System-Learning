import torch
import torch.nn as nn


T = 5
D = 8
MAX_SEQ_LEN = 16


position_ids = torch.arange(
    T
)


position_embedding = nn.Embedding(
    MAX_SEQ_LEN,
    D
)


pos = position_embedding(
    position_ids
)


print(
    "position ids:",
    position_ids.shape
)

print(
    "position embeddings:",
    pos.shape
)