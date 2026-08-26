from fastapi import FastAPI
from workers.inference_worker import task_queue
from models.request import ChatRequest
from concurrent.futures import Future

router = APIRouter()
# @app.post("/chat")
# def chat(request: ChatRequest):
#     return {
#         "reply": request.message
#     }

@app.post("/chat")
def chat(request: ChatRequest):
    future = Future()
    task = {
        "prompt": request.message
        "future": future
    }
    task_queue.put(task)
    result = future.result(timeout=30)
    return {
        "reply": result
    }

    