import torch
import torch.nn as nn


device = torch.device(
    "cuda"
)


model = nn.Linear(
    128,
    64
).to(
    device
)


x = torch.randn(
    32,
    128,
    device=device
)


with torch.autocast(
    device_type="cuda",
    dtype=torch.float16
):

    y = model(
        x
    )


print(
    y.dtype
)