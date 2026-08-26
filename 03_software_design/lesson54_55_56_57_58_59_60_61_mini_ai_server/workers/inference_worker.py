import threading
from queue import Queue
from services.llm_service import LLMService

service = LLMService()
task_queue = Queue()

def worker():
    while True:
        task = task_queue.get()

        try: 
            prompt = task["prompt"]
            future = task["future"]
            result = service.generate(prompt)
            future.set_result(result)
        except Exception as e:
            future.set_exception(e)
        finally:
            task_queue.task_done()


worker_thread = threading.Thread(
    target = worker
    daemon = True
)

worker_thread.start()

