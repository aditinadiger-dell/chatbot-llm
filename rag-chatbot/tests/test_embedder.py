import pytest
from src.chatbot.embedder import Embedder

def test_embedder_initialization():
    embedder = Embedder()
    assert embedder is not None

def test_text_embedding():
    embedder = Embedder()
    text = "This is a test sentence."
    embedding = embedder.embed(text)
    assert embedding is not None
    assert len(embedding) > 0

def test_batch_embedding():
    embedder = Embedder()
    texts = ["First sentence.", "Second sentence.", "Third sentence."]
    embeddings = embedder.embed_batch(texts)
    assert len(embeddings) == len(texts)
    for embedding in embeddings:
        assert embedding is not None
        assert len(embedding) > 0

def test_embedding_shape():
    embedder = Embedder()
    text = "Check the shape of the embedding."
    embedding = embedder.embed(text)
    assert len(embedding) == embedder.embedding_dimension  # Assuming embedding_dimension is defined in Embedder class