from src.services.embedding_service import EmbeddingService
from src.storage.vector_store import VectorStore
from src.services.ingestion_service import IngestionService

embedding_service = EmbeddingService()

vector_store = VectorStore(
    collection_name="learning"
)

ingestion_service = IngestionService(
    embedding_service,
    vector_store,
)

chunks = [
    "MongoDB stores patient and application data.",
    "HIPAA compliance ensures patient data security.",
    "Amazon Transcribe converts clinician speech into text.",
    "React Native was used to build the mobile application.",
]

metadata = {
    "source": "experiment_07"
}

ingestion_service.ingest(
    chunks,
    metadata
)

print(f"Chunks in collection: {vector_store.count_chunks()}")