def build_training_sequences(
    token_stream,
    seq_len
):

    samples = []


    chunk_size = (
        seq_len + 1
    )


    for start in range(
        0,
        len(token_stream) - chunk_size + 1,
        seq_len
    ):

        chunk = token_stream[
            start:
            start + chunk_size
        ]


        if len(chunk) != chunk_size:
            continue


        input_ids = chunk[:-1]

        targets = chunk[1:]


        samples.append(
            (
                input_ids,
                targets
            )
        )


    return samples