from services.llm_service import LLMService
from llms.fake import FakeLLM

def test_generate():
    llm = FakeLLM()
    service = LLMService(llm)
    result = service.generate("Hello")
    assert result == (
        "Fake Response: Hello"
    )

from unittest.mock import Mock


def test_generate():

    # Arrange
    mock_llm = Mock()
    mock_llm.generate.return_value = (
        "mock response"
    )
    service = LLMService(
        mock_llm
    )

    #Act
    result = service.generate(
        "hello"
    )

    #Assert
    assert result == "mock response"
    mock_llm.generate.assert_called_once_with(
        "hello"
    )

