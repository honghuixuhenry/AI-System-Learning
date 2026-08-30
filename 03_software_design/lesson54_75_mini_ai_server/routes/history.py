from fastapi import APIRouter

from database.repository import (
    ChatHistoryRepository
)

router = APIRouter()

repository = (
    ChatHistoryRepository()
)

@router.get("/history")
def history():
    return repository.get_call()