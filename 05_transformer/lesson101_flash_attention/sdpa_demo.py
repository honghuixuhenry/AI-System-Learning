import torch
import torch.nn.functional as F


B = 2
H = 4
T = 8
HEAD_DIM = 16


q = torch.randn(
    B,
    H,
    T,
    HEAD_DIM
)


k = torch.randn(
    B,
    H,
    T,
    HEAD_DIM
)


v = torch.randn(
    B,
    H,
    T,
    HEAD_DIM
)


output = (
    F.scaled_dot_product_attention(
        q,
        k,
        v,
        is_causal=True
    )
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

print(
    "Output:",
    output.shape
)