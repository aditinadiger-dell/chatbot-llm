import unittest
from src.chatbot.retriever import Retriever

class TestRetriever(unittest.TestCase):

    def setUp(self):
        self.retriever = Retriever()
        self.sample_query = "What is retrieval-augmented generation?"
        self.expected_output = ["Retrieval-augmented generation (RAG) is a framework that combines retrieval and generation for improved performance."]

    def test_retrieve(self):
        result = self.retriever.retrieve(self.sample_query)
        self.assertIn(self.expected_output[0], result)

    def test_empty_query(self):
        result = self.retriever.retrieve("")
        self.assertEqual(result, [])

    def test_invalid_query(self):
        result = self.retriever.retrieve("nonexistent query")
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()