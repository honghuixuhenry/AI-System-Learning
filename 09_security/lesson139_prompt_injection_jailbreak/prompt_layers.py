from dataclasses import dataclass
from typing import List


@dataclass
class PromptSegment:
    source: str
    content: str
    trusted: bool


def build_context(
    system_instruction: str,
    user_input: str,
    retrieved_documents: List[str]
):

    segments = [
        PromptSegment(
            source="system",
            content=system_instruction,
            trusted=True
        ),

        PromptSegment(
            source="user",
            content=user_input,
            trusted=False
        )
    ]

    for document in retrieved_documents:

        segments.append(
            PromptSegment(
                source="retrieved_document",
                content=document,
                trusted=False
            )
        )

    return segments