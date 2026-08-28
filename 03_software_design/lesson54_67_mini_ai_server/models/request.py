from pydantic import BaseModel

class ChatRequest(BaseModel):
    message: str
    temperature: float
    max_tokens: int
    reply: str
    tokens: int
