import os

class Settings:
    EMBEDDING_MODEL: str = os.getenv(
        "EMBEDDING_MODEL",
        "all-MiniLM-L6-v2"
    )
    CHROMA_DB_PATH: str = os.getenv(
        "CHROMA_DB_PATH",
        "./chroma_data"
    )
    COLLECTION_NAME: str = os.getenv(
        "COLLECTION_NAME",
        "test_collection"
    )

settings = Settings()
