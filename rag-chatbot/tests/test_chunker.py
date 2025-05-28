import unittest
from src.chatbot.chunker import Chunker

class TestChunker(unittest.TestCase):

    def setUp(self):
        self.chunker = Chunker()

    def test_chunk_text(self):
        text = "This is a sample text that needs to be chunked into smaller parts."
        expected_chunks = [
            "This is a sample text",
            "that needs to be chunked",
            "into smaller parts."
        ]
        chunks = self.chunker.chunk_text(text, chunk_size=10)
        self.assertEqual(chunks, expected_chunks)

    def test_chunk_empty_text(self):
        text = ""
        expected_chunks = []
        chunks = self.chunker.chunk_text(text, chunk_size=10)
        self.assertEqual(chunks, expected_chunks)

    def test_chunk_text_with_special_characters(self):
        text = "Hello! This is a test. Let's see how it handles: punctuation, numbers (123), and symbols #$%&."
        expected_chunks = [
            "Hello! This is a test.",
            "Let's see how it handles:",
            "punctuation, numbers (123),",
            "and symbols #$%&."
        ]
        chunks = self.chunker.chunk_text(text, chunk_size=15)
        self.assertEqual(chunks, expected_chunks)

if __name__ == '__main__':
    unittest.main()