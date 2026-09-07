from cleaning_demo import (
    clean_text
)

from sequence_builder import (
    build_sequences
)


def prepare_training_data(
    raw_documents,
    tokenizer,
    seq_len
):

    cleaned_documents = []


    for document in raw_documents:

        document = clean_text(
            document
        )

        if not document:
            continue

        cleaned_documents.append(
            document
        )


    token_stream = []


    for document in (
        cleaned_documents
    ):

        token_ids = tokenizer.encode(
            document
        )

        token_stream.extend(
            token_ids
        )


    sequences = build_sequences(
        token_stream,
        seq_len
    )


    return sequences