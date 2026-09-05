import torch


B = 2
T = 5

NUM_Q_HEADS = 8
NUM_KV_HEADS = 1

HEAD_DIM = 16


q = torch.randn(
    B,
    NUM_Q_HEADS,
    T,
    HEAD_DIM
)


k = torch.randn(
    B,
    NUM_KV_HEADS,
    T,
    HEAD_DIM
)


v = torch.randn(
    B,
    NUM_KV_HEADS,
    T,
    HEAD_DIM
)


print(
    "Q:",
    q.shape
)

print(
    "K:",
    k.shape
)

print(
    "V:",
    v.shape
)