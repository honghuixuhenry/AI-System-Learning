class RAGAgent:

    def __init__(
        self,
        retriever,
        context_builder
    ):
        self.retriever = (
            retriever
        )

        self.context_builder = (
            context_builder
        )


    def answer(
        self,
        query
    ):

        documents = (
            self.retriever.search(
                query,
                top_k=2
            )
        )

        prompt = (
            self.context_builder.build(
                query,
                documents
            )
        )

        return {
            "documents": documents,
            "prompt": prompt
        }