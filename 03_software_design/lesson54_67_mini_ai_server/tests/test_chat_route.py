from fastapi.testclient import TestClient
from app import app
from dependencies.services import (
    get_llm_service
)
from services.llm_service import (
    LLMService
)
from llms.fake import FakeLLM

def get_fake_llm_service():
    return LLMService(FakeLLM())

app.dependency_overrides[
    get_llm_service
] = get_fake_llm_service

client = TestClient(app)

def test_chat():
    reponse = client.post(
        "/chat",
        json = {
            "message": "Hello"
        }
    )

    assert reponse.status_code == 200
    assert reponse.json() == {
        "reply": "Fake response: Hello"
    }