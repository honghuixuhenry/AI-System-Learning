def build_sequences(
    token_ids,
    seq_len
):

    sequences = []


    for start in range(
        0,
        len(token_ids) - seq_len,
        seq_len
    ):

        chunk = token_ids[
            start:
            start
            +
            seq_len
            +
            1
        ]


        if len(chunk) < (
            seq_len + 1
        ):
            break


        x = chunk[:-1]

        target = chunk[1:]


        sequences.append(
            (
                x,
                target
            )
        )


    return sequences