from dataclasses import dataclass

@dataclass
class DocumentChunk:
    id: str
    text: str
    embedding: list[float] | None = None
    metadata: dict[str, str]