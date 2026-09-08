class KnowledgeService:

    def __init__(self):

        self.documents = {
            "transformer":
                "Transformers use attention.",

            "agent":
                "Agents combine models, "
                "tools and runtime control."
        }

        self.memory = {}


    def search(
        self,
        query: str
    ):

        query = query.lower()

        results = []

        for key, text in (
            self.documents.items()
        ):

            if key in query:
                results.append(text)

        return results