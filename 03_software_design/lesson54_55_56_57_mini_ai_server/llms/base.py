from abc import ABC, abstractmenthod

class LLM(ABC):
    @abstractmenthod
    def generate(self, prompt: str) -> str:
        pass