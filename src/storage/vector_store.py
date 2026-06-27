import chromadb

from src.config import settings
from src.models.document_chunk import DocumentChunk

class VectorStore:
    def __init__(self, collection_name: str):
        self._client = chromadb.PersistentClient(
            path=settings.CHROMA_DB_PATH
        )

        self._collection = self._client.get_or_create_collection(
            name=collection_name
        )

    def add_chunks(self, chunks: list[DocumentChunk]):
        
        if not chunks:
            return

        ids = []
        documents = []
        embeddings = []
        metadatas = []

        for chunk in chunks:
            ids.append(chunk.id)
            documents.append(chunk.text)
            embeddings.append(chunk.embedding)
            metadatas.append(chunk.metadata)

        self._collection.add(
            ids=ids,
            documents=documents,
            embeddings=embeddings,
            metadatas=metadatas,
        )