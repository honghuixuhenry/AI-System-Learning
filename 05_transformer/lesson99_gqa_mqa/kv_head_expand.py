import torch


B = 1
T = 3

NUM_Q_HEADS = 8
NUM_KV_HEADS = 2
HEAD_DIM = 4


group_size = (
    NUM_Q_HEADS
    //
    NUM_KV_HEADS
)


k = torch.randn(
    B,
    NUM_KV_HEADS,
    T,
    HEAD_DIM
)


k_expanded = (
    k.repeat_interleave(
        group_size,
        dim=1
    )
)


print(
    "original K:",
    k.shape
)

print(
    "expanded K:",
    k_expanded.shape
)