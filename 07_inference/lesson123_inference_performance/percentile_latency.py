import torch


latencies = torch.tensor([
    100.0,
    110.0,
    95.0,
    120.0,
    105.0,
    200.0,
    500.0,
    1000.0
])


for percentile in [
    0.50,
    0.90,
    0.95,
    0.99
]:

    value = torch.quantile(
        latencies,
        percentile
    )

    print(
        percentile,
        value.item()
    )