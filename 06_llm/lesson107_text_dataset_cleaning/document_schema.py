from dataclasses import dataclass
from typing import Optional


@dataclass
class Document:

    document_id: str

    text: str

    source: str

    language: Optional[str] = None

    quality_score: Optional[float] = None


documents = [

    Document(
        document_id="1",
        text="""
        Artificial    intelligence
        is changing computing.
        """,
        source="web"
    ),

    Document(
        document_id="2",
        text="BUY BUY BUY BUY BUY!!!",
        source="web"
    ),

    Document(
        document_id="3",
        text="Transformer models use attention.",
        source="book"
    ),

    Document(
        document_id="4",
        text="Transformer models use attention.",
        source="web"
    ),
]