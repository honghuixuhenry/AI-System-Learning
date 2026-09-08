from documents import DOCUMENTS

from retriever import (
    KeywordRetriever
)

from context_builder import (
    ContextBuilder
)

from rag_agent import (
    RAGAgent
)


retriever = KeywordRetriever(
    DOCUMENTS
)

builder = ContextBuilder()

agent = RAGAgent(
    retriever,
    builder
)


result = agent.answer(
    "What is the hotel "
    "reimbursement limit?"
)


print(
    "Retrieved documents:"
)

for document in result[
    "documents"
]:
    print(
        document
    )


print(
    "\nPrompt:"
)

print(
    result["prompt"]
)