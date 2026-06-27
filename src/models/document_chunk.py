from dataclasses import dataclass


@dataclass
class DocumentChunk:
    id: str
    text: str
    embedding: list[float]
    metadata: dict[str, str]