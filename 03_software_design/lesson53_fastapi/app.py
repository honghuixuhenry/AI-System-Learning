from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello AI System"}

@app.get("/user/{user_id}")
def get_user(user_id: int):
    return {
        "user_id": user_id
    }

@app.get("/search")
def search(keyword: str):
    return {
        "keyword": keyword
    }

from pydantic import BaseModel

class Prompt(BaseModel):
    message: str

@app.post("/chat")
def chat(prompt: Prompt):
    return {
        "reply": f"You said: {prompt.message}"
    }

@app.post("/generate")
def generate(prompt: Prompt):
    output = model.generate(prompt.message)
    return {
        "response": output
    }