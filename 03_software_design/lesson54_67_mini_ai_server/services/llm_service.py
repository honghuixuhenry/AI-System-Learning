# class LLMService:
#     def generate(self, prompt):
#         return "Hello from LLM"

from config.config import MODEL_NAME
from llms.factory import LLMFactory

class LLMService:
    def __init__(self, llm, cache):
        self.llm = llm
        self.cache = cache

    def generate(self, prompt: str) -> str:
        cached_result = self.cache.get()

        if cached_result is not None:
            print("Cache HIT")
            return cached_result
        print ("Cache MISS")

        result = self.llm.generate(prompt)
        self.cache.set(prompt, result)
        return result