PAD_ID = 0
BOS_ID = 1
EOS_ID = 2
UNK_ID = 3


sentence_ids = [
    4,
    5,
    6
]


with_special_tokens = [
    BOS_ID,
    *sentence_ids,
    EOS_ID
]


print(
    with_special_tokens
)