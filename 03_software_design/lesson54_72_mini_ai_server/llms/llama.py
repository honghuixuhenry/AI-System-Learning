from llms.base import LLM
class Llama(LLM):
    def generate(self, prompt):
        return f"Llama: {prompt}"

    