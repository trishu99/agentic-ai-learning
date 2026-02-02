from sentence_transformers import SentenceTransformer
import faiss
import numpy as np


class PersonalAssistantMemory:
    def __init__(self, embedding_model_name="all-MiniLM-L6-v2"):
        # Load embedding model
        self.model = SentenceTransformer(embedding_model_name)

        # Memory storage
        self.memories = []

        # FAISS index (initialized lazily)
        self.index = None
        self.embedding_dim = None

    def add_memory(self, text: str):
        """
        Stores a memory and updates the vector index
        """
        embedding = self.model.encode([text])
        embedding = np.asarray(embedding).astype("float32")

        # Initialize index on first insert
        if self.index is None:
            self.embedding_dim = embedding.shape[1]
            self.index = faiss.IndexFlatL2(self.embedding_dim)

        self.index.add(embedding)
        self.memories.append(text)

        print(f"🧠 Memory added: {text}")

    def recall(self, query: str, k: int = 3):
        """
        Retrieves top-k relevant memories
        """
        if not self.memories:
            return []

        query_embedding = self.model.encode([query])
        query_embedding = np.asarray(query_embedding).astype("float32")

        distances, indices = self.index.search(query_embedding, k)

        results = []
        for idx in indices[0]:
            if idx < len(self.memories):
                results.append(self.memories[idx])

        return results


# 🧪 Demo usage
if __name__ == "__main__":
    assistant = PersonalAssistantMemory()

    # Add memories
    assistant.add_memory("User likes concise answers")
    assistant.add_memory("User prefers Python examples")
    assistant.add_memory("User works on Agentic AI systems")

    print("\n🔍 Querying memory...\n")

    query = "How should I explain FAISS?"
    recalled_memories = assistant.recall(query)

    for memory in recalled_memories:
        print(f"- {memory}")
