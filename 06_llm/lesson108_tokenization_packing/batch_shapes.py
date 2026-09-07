import torch


samples = [
    (
        [1,2,3,4],
        [2,3,4,5]
    ),

    (
        [6,7,8,9],
        [7,8,9,10]
    ),
]


inputs = torch.tensor(
    [
        x
        for x, _
        in samples
    ],
    dtype=torch.long
)


targets = torch.tensor(
    [
        y
        for _, y
        in samples
    ],
    dtype=torch.long
)


print(
    "inputs:",
    inputs.shape
)

print(
    "targets:",
    targets.shape
)