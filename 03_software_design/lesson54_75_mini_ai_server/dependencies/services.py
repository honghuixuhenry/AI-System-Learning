from services.llm_service import LLMService
from fastapi import Request

def get_llm_service(
        request: Request
) -> LLMService:
    llm = request.app.state.llm
    return LLMService(llm)
