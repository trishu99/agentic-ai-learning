class LongTermMemory:
    def __init__(self, index, texts):
        self.index = index
        self.texts = texts

    def retrieve(self, query_embedding, k=1):
        distances, indices = self.index.search(query_embedding, k)
        return [self.texts[i] for i in indices[0]]
