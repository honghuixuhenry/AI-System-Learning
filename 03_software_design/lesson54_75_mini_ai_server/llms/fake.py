from llms.base import LLM

class FakeLLM(LLM):
    def generate(self, prompt: str) -> str:
        return f"Fake response: {prompt}"