import torch


batch = 2
input_dim = 6
output_dim = 4


y = torch.randn(
    batch,
    input_dim
)


w = torch.randn(
    input_dim,
    output_dim
)


y0, y1 = torch.chunk(
    y,
    chunks=2,
    dim=1
)


w0, w1 = torch.chunk(
    w,
    chunks=2,
    dim=0
)


z0 = y0 @ w0
z1 = y1 @ w1


z_tp = z0 + z1


z_full = y @ w


print(
    torch.allclose(
        z_tp,
        z_full
    )
)