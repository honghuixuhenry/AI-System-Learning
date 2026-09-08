DOCUMENTS = [
    {
        "id": "doc1",
        "text": (
            "Local LLM inference can "
            "reduce the need to send "
            "sensitive data to remote servers."
        )
    },
    {
        "id": "doc2",
        "text": (
            "Local inference can continue "
            "working when network connectivity "
            "is limited."
        )
    },
    {
        "id": "doc3",
        "text": (
            "Large language models may require "
            "significant memory and computing "
            "resources when deployed locally."
        )
    },
    {
        "id": "doc4",
        "text": (
            "Local deployment may reduce "
            "network latency, but inference "
            "latency still depends on hardware "
            "and model size."
        )
    }
]

class Retriever:

    def __init__(
        self,
        documents
    ):
        self.documents = documents


    def retrieve(
        self,
        query,
        top_k=3
    ):

        query_words = set(
            query.lower().split()
        )

        scored = []

        for document in self.documents:

            document_words = set(
                document[
                    "text"
                ].lower().split()
            )

            score = len(
                query_words
                &
                document_words
            )

            scored.append(
                (
                    score,
                    document
                )
            )

        scored.sort(
            key=lambda item:
                item[0],
            reverse=True
        )

        return [
            document
            for score, document
            in scored[:top_k]
            if score > 0
        ]