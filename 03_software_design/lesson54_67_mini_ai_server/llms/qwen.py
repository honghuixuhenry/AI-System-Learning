from llms.base import LLM

class Qwen(LLM):
    def generate(self, prompt):
        return f"Qwen: {prompt}"