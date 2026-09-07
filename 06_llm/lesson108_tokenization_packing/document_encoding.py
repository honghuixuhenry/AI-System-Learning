def encode_documents(
    documents,
    tokenizer
):

    encoded_documents = []


    for document in documents:

        token_ids = tokenizer.encode(
            document,
            add_eos=True
        )

        encoded_documents.append(
            token_ids
        )


    return encoded_documents

def build_token_stream(
    encoded_documents
):

    token_stream = []


    for token_ids in encoded_documents:

        token_stream.extend(
            token_ids
        )


    return token_stream


documents = [
    "AI models learn from data",
    "AI models learn",
    "models learn from data",
]

