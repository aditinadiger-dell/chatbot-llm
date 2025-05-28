class Chunker:
    def __init__(self, chunk_size=100):
        self.chunk_size = chunk_size

    def chunk_text(self, text):
        """Divides the input text into manageable chunks."""
        words = text.split()
        return [' '.join(words[i:i + self.chunk_size]) for i in range(0, len(words), self.chunk_size)]

    def chunk_data(self, data):
        """Chunks a list of texts."""
        return [self.chunk_text(text) for text in data]