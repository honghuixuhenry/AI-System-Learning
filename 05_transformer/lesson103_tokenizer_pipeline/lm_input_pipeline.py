import torch


PAD_ID = 0
BOS_ID = 1
EOS_ID = 2
UNK_ID = 3


vocab = {
    "<pad>": PAD_ID,
    "<bos>": BOS_ID,
    "<eos>": EOS_ID,
    "<unk>": UNK_ID,
    "I": 4,
    "love": 5,
    "AI": 6,
    "is": 7,
    "powerful": 8,
}


def encode(
    text,
    add_special_tokens=True
):

    tokens = text.split()

    ids = [
        vocab.get(
            token,
            UNK_ID
        )
        for token in tokens
    ]

    if add_special_tokens:

        ids = [
            BOS_ID,
            *ids,
            EOS_ID
        ]

    return ids

def make_batch(
    texts
):

    encoded = [
        encode(text)
        for text in texts
    ]


    max_len = max(
        len(ids)
        for ids in encoded
    )


    padded = []


    for ids in encoded:

        padding_length = (
            max_len
            -
            len(ids)
        )

        padded_ids = (
            ids
            +
            [PAD_ID]
            *
            padding_length
        )

        padded.append(
            padded_ids
        )


    input_ids = torch.tensor(
        padded,
        dtype=torch.long
    )


    attention_mask = (
        input_ids
        !=
        PAD_ID
    )


    return (
        input_ids,
        attention_mask
    )

texts = [
    "I love AI",
    "AI is powerful",
    "AI"
]


input_ids, attention_mask = (
    make_batch(
        texts
    )
)


print(
    "input_ids:"
)

print(
    input_ids
)


print(
    "attention_mask:"
)

print(
    attention_mask
)