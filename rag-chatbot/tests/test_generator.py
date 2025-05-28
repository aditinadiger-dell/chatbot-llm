import unittest
from src.chatbot.generator import Generator

class TestGenerator(unittest.TestCase):

    def setUp(self):
        self.generator = Generator()

    def test_generate_response(self):
        retrieved_info = "This is a test information chunk."
        response = self.generator.generate_response(retrieved_info)
        self.assertIsInstance(response, str)
        self.assertGreater(len(response), 0)

    def test_generate_response_empty_input(self):
        response = self.generator.generate_response("")
        self.assertEqual(response, "I'm sorry, I couldn't generate a response.")

if __name__ == '__main__':
    unittest.main()