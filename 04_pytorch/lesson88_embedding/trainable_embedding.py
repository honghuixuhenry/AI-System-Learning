import torch
import torch.nn as nn
import torch.optim as optim


embedding = nn.Embedding(
    5,
    3
)


optimizer = optim.SGD(
    embedding.parameters(),
    lr=0.1
)


token_ids = torch.tensor(
    [1,2]
)


before = (
    embedding.weight
    .detach()
    .clone()
)


vectors = embedding(
    token_ids
)


loss = vectors.sum()


optimizer.zero_grad()

loss.backward()

optimizer.step()


after = (
    embedding.weight
    .detach()
    .clone()
)


print(
    "Before:"
)

print(before)

print(
    "After:"
)

print(after)