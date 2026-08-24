from llms.qwen import Qwen
from llms.deepseek import DeepSeek
from llms.llama import Llama

class LLMFactory:
    @staticmethod
    def create(model_name: str):
        if model_name == "Qwen":
            return Qwen()
        elif model_name == "Llama":
            return Llama()
        elif model_name == "DeepSeek":
            return DeepSeek()
        else: 
            raise ValueError("Unknown model")