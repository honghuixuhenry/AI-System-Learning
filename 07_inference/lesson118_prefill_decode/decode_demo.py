import torch


batch_size = 1


prompt_tokens = torch.tensor([
    [
        10,
        20,
        30,
        40
    ]
])


print(
    "Prefill input:",
    prompt_tokens.shape
)


next_token = torch.tensor([
    [50]
])


print(
    "Decode input:",
    next_token.shape
)