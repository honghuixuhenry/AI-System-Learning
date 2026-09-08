from dataclasses import dataclass


@dataclass
class EmbeddingRequest:
    text: str


@dataclass
class EmbeddingResponse:
    dimensions: int
    values: list