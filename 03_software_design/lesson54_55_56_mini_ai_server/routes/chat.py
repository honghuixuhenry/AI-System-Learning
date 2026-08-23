from fastapi import FastAPI
from models.request import ChatRequest
from services.llm_service import LLMService

app = FastAPI()

service = LLMService()

reply = service.generate()

@app.post("/chat")
def chat(request: ChatRequest):
    return {
        "reply": request.message
    }

@app.post("/chat")
def LLMreply():
    return {
        "LLL reply": reply
    }