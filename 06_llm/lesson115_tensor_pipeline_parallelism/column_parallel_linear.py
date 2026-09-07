import torch


batch = 2
input_dim = 4
output_dim = 6


x = torch.randn(
    batch,
    input_dim
)


w = torch.randn(
    input_dim,
    output_dim
)


w0, w1 = torch.chunk(
    w,
    chunks=2,
    dim=1
)


y0 = x @ w0
y1 = x @ w1


y_tp = torch.cat(
    [y0, y1],
    dim=1
)


y_full = x @ w


print(
    torch.allclose(
        y_tp,
        y_full
    )
)