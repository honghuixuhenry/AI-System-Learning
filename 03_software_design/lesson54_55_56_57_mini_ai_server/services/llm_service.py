# class LLMService:
#     def generate(self, prompt):
#         return "Hello from LLM"

from config.config import MODEL_NAME
from llms.factory import LLMFactory

class LLMService:
    def __init__(self):
        self.llm = LLMFactory.create(MODEL_NAME)

    def generate(self, prompt):
        return self.llm.generate(prompt)