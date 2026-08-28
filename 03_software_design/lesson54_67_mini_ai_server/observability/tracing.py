import time

class Span:
    def __init__(self, name):
        self.name = name
    def __enter__(self):
        self.start = time.perf_counter()
        print(
            f"{self.name} started"
        )
        return self
    def __exit__(self, exc_type, exc, tb):
        duration = (time.perf_counter() - self.start)
        print(
            f"{self.name}: "
            f"{duration: 3f}s"
        )

def fake_llm(prompt):
    time.sleep(2)

# start = time.perf_counter()
# result = fake_llm("Hello")
# latency = time.perf_counter() - start

# with Span("LLM"):
#     fake_llm("Hello")

with Span("Request"):
    with Span("Cache"):
        time.sleep(0.1)
    with Span("LLM"):
        time.sleep(2)
    with Span("Tool"):
        time.sleep(1)