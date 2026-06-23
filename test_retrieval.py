from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

question = "How was speech converted into notes?"

embedding = model.encode(question)

print(type(embedding))
print(len(embedding))
print(embedding[:10])