from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim
from bells_chunks import chunks

model = SentenceTransformer("all-MiniLM-L6-v2")

question = "How was speech converted into notes?"

question_embedding = model.encode(question)

print(f"\nQuestion: {question}\n")

chunk_embeddings = []

for chunk in chunks:
    chunk_embeddings.append({
        "text": chunk,
        "embedding": model.encode(chunk)
    })

similarity = cos_sim(
    question_embedding,
    chunk_embeddings
)