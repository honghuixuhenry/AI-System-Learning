import torch


tokens = torch.tensor(
    [
        10,
        20,
        30,
        40,
        50
    ],
    dtype=torch.long
)


input_ids = tokens[:-1]

targets = tokens[1:]


print(
    "tokens:",
    tokens
)

print(
    "input_ids:",
    input_ids
)

print(
    "targets:",
    targets
)