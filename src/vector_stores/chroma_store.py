import chromadb

from src.config import settings


class ChromaStore:
    def __init__(self):
        self._client = chromadb.PersistentClient(
            path=settings.CHROMA_DB_PATH
        )

        self._collection = self._client.get_or_create_collection(
            name=settings.COLLECTION_NAME
        )