import torch


B = 2
T = 6

NUM_Q_HEADS = 8
NUM_KV_HEADS = 2

HEAD_DIM = 16


assert (
    NUM_Q_HEADS
    %
    NUM_KV_HEADS
    ==
    0
)


GROUP_SIZE = (
    NUM_Q_HEADS
    //
    NUM_KV_HEADS
)


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
    "group size:",
    GROUP_SIZE
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