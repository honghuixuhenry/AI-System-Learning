import torch
import torch.nn as nn


x = torch.tensor([
    [
        [1.0, 2.0, 3.0, 4.0]
    ]
])


layer_norm = nn.LayerNorm(
    4,
    elementwise_affine=False
)


rms_norm = RMSNorm(
    4
)


with torch.no_grad():

    rms_norm.weight.fill_(
        1.0
    )


ln_output = layer_norm(
    x
)


rms_output = rms_norm(
    x
)


print(
    "input:",
    x
)

print(
    "LayerNorm:",
    ln_output
)

print(
    "RMSNorm:",
    rms_output
)