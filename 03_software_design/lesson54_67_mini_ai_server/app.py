from contextlib import asynccontextmanager
from fastapi import FastAPI
from llms.qwen import Qwen
from routes.chat import router

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting AI Server ... ")
    app.state.llm = Qwen()
    print("Model loaded")
    yield
    print("Shutting down AI Server")
    app.state.llm = None
    print("Resource released")

app = FastAPI(
    lifespan = lifespan
)
app.include_router(router)
