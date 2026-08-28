from fastapi import FastAPI, APIRouter
from fastapi import Depends, HTTPException
from services.llm_service import LLMService
from dependencies.services import get_llm_service
from workers.inference_worker import task_queue
from models.request import ChatRequest
from concurrent.futures import Future
from queue import Full

router = APIRouter()
@router.post("/chat")
def chat(request: ChatRequest, service: LLMService = Depends(get_llm_service)):
    return {
        "reply": service.generate(request.message)
    }

@router.post("/chat")
def chat(request: ChatRequest):
    future = Future()
    task = {
        "prompt": request.message,
        "future": future
    }
    try:
        task_queue.put_nowait(task, timeout = 2)
    except Full:
        raise HTTPException(
            status_code = 503, 
            details = "Server is busy"
        )
    try:
        result = future.result(timeout=30)
    except TimeoutError:
        raise HTTPException(
            status_code=504,
            detail="Inference Timeout"
        )
    return {
        "reply": result
    }

    