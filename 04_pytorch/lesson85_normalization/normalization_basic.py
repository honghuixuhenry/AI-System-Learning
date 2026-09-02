import torch


x = torch.tensor([
    1.0,
    2.0,
    3.0,
    4.0
])


mean = x.mean()

variance = x.var(
    unbiased=False
)


x_norm = (
    x - mean
) / torch.sqrt(
    variance + 1e-5
)


print("mean:", mean)

print(
    "variance:",
    variance
)

print(
    "normalized:",
    x_norm
)

print(
    "new mean:",
    x_norm.mean()
)

print(
    "new variance:",
    x_norm.var(
        unbiased=False
    )
)