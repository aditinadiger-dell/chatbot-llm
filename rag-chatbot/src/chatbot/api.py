from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from chatbot.retriever import Retriever
from chatbot.generator import Generator

app = FastAPI()

class Query(BaseModel):
    question: str

retriever = Retriever()
generator = Generator()

@app.post("/chat")
async def chat(query: Query):
    try:
        retrieved_chunks = retriever.retrieve(query.question)
        response = generator.generate(retrieved_chunks)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))