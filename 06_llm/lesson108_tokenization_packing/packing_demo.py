def pack_documents(
    encoded_documents,
    seq_len
):

    token_stream = []


    for token_ids in (
        encoded_documents
    ):

        token_stream.extend(
            token_ids
        )


    samples = []


    for start in range(
        0,
        len(token_stream) - seq_len,
        seq_len
    ):

        chunk = token_stream[
            start:
            start + seq_len + 1
        ]


        if (
            len(chunk)
            <
            seq_len + 1
        ):
            break


        input_ids = chunk[:-1]

        targets = chunk[1:]


        samples.append(
            (
                input_ids,
                targets
            )
        )


    return samples

for i, (
    input_ids,
    targets
) in enumerate(samples):

    print(
        "Sample:",
        i
    )

    print(
        "Input:",
        input_ids
    )

    print(
        "Target:",
        targets
    )