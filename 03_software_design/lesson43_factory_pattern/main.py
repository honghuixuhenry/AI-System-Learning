class LLMFactory:
    def create(model):
        if model == "Qwen":
            return Qwen()
        elif model == "Llama":
            return Llama()
        elif model == "DeepSeek":
            return DeepSeek()
        else:
            raise ValueError("Unknown Model")

class LLM:
    def __init__(self):
        pass
class DeepSeek(LLM):
    def generate(self, prompt):
        return "Deepseek Response"
class Qwen(LLM):
    def generate(self, prompt):
        return "Qwen Response"
class Llama(LLM):
    def generate(self, prompt):
        return "Llama Response"

class Agent:
    def __init__(self, llm):
        self.llm = llm
    def run(self, prompt):
        return self.llm.generate(prompt)

llm = LLMFactory.create("DeepSeek")
agent = Agent(llm)
print(agent.run("hello"))

