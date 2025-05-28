class Embedder:
    def __init__(self, model):
        self.model = model

    def embed(self, text):
        """
        Convert text data into embeddings using the specified model.
        """
        return self.model.encode(text)

    def embed_batch(self, texts):
        """
        Convert a batch of text data into embeddings.
        """
        return [self.embed(text) for text in texts]