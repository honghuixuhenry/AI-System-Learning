from fastapi import FastAPI, APIRouter
from fastapi import Depends, HTTPException, Header
from services.llm_service import LLMService
from dependencies.services import get_llm_service
from workers.inference_worker import task_queue
from models.request import ChatRequest
from concurrent.futures import Future
from queue import Full
import uuid 
import logging
from security.api_key import verify_api_key
from dependencies.auth import authenticate

logger = logging.getLogger(__name__)
router = APIRouter()


@router.get("/protected")
def chat(
    request: ChatRequest,
    user = Depends(authenticate),
    service: LLMService = Depends(get_llm_service)
):
    result = service.generate(
        request.message
    )
    return {
        "user": user["username"],
        "reply": result
    }

@router.post("/chat")
def chat(request: ChatRequest, service: LLMService = Depends(get_llm_service)):
    return {
        "reply": service.generate(request.message)
    }

@router.post("/chat")
def chat(request: ChatRequest):
    request_id = str(uuid.uuid4())[:8]

    logger.info(
        f"[{request_id}] Request received"
    )

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
        logger.info(
            f"[{request_id}] Request completed"
        )
    except TimeoutError:
        raise HTTPException(
            status_code=504,
            detail="Inference Timeout"
        )
    return {
        "request_id": request_id,
        "reply": result
    }

