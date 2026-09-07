max_sequence_length = 4096


requests = {
    "A": 700,
    "B": 1300,
    "C": 250
}


for request_id, used_tokens in requests.items():

    wasted = (
        max_sequence_length
        -
        used_tokens
    )

    print(
        request_id,
        "used:",
        used_tokens,
        "allocated:",
        max_sequence_length,
        "wasted:",
        wasted
    )