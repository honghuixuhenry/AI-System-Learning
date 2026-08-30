from llms.base import LLM
class DeepSeek(LLM):
    def generate(self, prompt):
        return f"DeepSeek: {prompt}"