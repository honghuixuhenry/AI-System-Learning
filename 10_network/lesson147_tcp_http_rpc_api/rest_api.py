DOCUMENTS = {
    "1": "Transformer notes",
    "2": "Agent security notes"
}


def get_document(
    document_id: str
):

    return DOCUMENTS.get(
        document_id
    )


def create_document(
    document_id: str,
    text: str
):

    DOCUMENTS[
        document_id
    ] = text

    return {
        "created":
            document_id
    }