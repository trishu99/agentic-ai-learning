from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

memory = [
    "User likes concise answers",
    "User prefers Python",
]

embeddings = model.encode(memory)
embeddings = np.asarray(embeddings).astype("float32")

index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)

# 🔍 Query
query = "I like short Python answers"
query_embedding = model.encode([query])
query_embedding = np.asarray(query_embedding).astype("float32")

distances, indices = index.search(query_embedding, k=2)

for idx in indices[0]:
    print(memory[idx])


'''
retrieve memory by meaning, not keywords.
'''