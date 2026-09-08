class ContextBuilder:

    def build(
        self,
        query,
        documents
    ):

        context_parts = []

        for document in documents:

            context_parts.append(
                document["text"]
            )

        context = "\n\n".join(
            context_parts
        )

        prompt = f"""
Use the following context
to answer the question.

Context:
{context}

Question:
{query}
"""

        return prompt