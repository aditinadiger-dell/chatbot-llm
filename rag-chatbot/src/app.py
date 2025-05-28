from flask import Flask, request, jsonify
from chatbot.retriever import Retriever
from chatbot.generator import Generator
from chatbot.chunker import Chunker
from chatbot.embedder import Embedder

app = Flask(__name__)

# Initialize components
retriever = Retriever()
generator = Generator()
chunker = Chunker()
embedder = Embedder()

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    if not user_input:
        return jsonify({'error': 'No message provided'}), 400

    # Chunk the input
    chunks = chunker.chunk(user_input)

    # Retrieve relevant information
    relevant_chunks = retriever.retrieve(chunks)

    # Generate a response
    response = generator.generate(relevant_chunks)

    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)