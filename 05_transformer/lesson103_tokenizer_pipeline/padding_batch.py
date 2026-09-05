import torch


PAD_ID = 0


sequences = [
    [4, 5, 6],
    [6, 7, 8],
    [9],
]


max_len = max(
    len(seq)
    for seq in sequences
)


padded = []


for seq in sequences:

    num_padding = (
        max_len
        -
        len(seq)
    )

    padded_seq = (
        seq
        +
        [PAD_ID]
        *
        num_padding
    )

    padded.append(
        padded_seq
    )


batch = torch.tensor(
    padded,
    dtype=torch.long
)


print(
    batch
)


print(
    batch.shape
)