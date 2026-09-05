import torch


PAD_ID = 0


input_ids = torch.tensor(
    [
        [4, 5, 6],
        [6, 7, 8],
        [9, 0, 0],
    ],
    dtype=torch.long
)


attention_mask = (
    input_ids
    !=
    PAD_ID
)


print(
    attention_mask
)