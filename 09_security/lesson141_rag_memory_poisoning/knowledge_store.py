from dataclasses import dataclass
from typing import List


@dataclass
class Document:
    document_id: str
    source: str
    text: str
    trusted: bool = False


DOCUMENTS: List[Document] = [
    Document(
        document_id="doc-001",
        source="official_policy",
        text=(
            "Travel expenses must be "
            "submitted within 30 days."
        ),
        trusted=True
    ),

    Document(
        document_id="doc-002",
        source="official_policy",
        text=(
            "Hotel reimbursement is "
            "limited to $220 per night."
        ),
        trusted=True
    )
]