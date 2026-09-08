class KeywordRetriever:

    def __init__(
        self,
        documents
    ):
        self.documents = documents


    def search(
        self,
        query,
        top_k=2
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
            key=lambda item: item[0],
            reverse=True
        )

        return [
            document
            for score, document
            in scored[:top_k]
            if score > 0
        ]