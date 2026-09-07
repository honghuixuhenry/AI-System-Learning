from request import Request
from request_queue import (
    RequestQueue
)
from scheduler import Scheduler
from kv_cache import KVCache
from model_runtime import (
    ToyModelRuntime
)
from inference_engine import (
    InferenceEngine
)


queue = RequestQueue()

scheduler = Scheduler(
    max_batch_size=2
)

kv_cache = KVCache()

runtime = ToyModelRuntime()


engine = InferenceEngine(
    scheduler=scheduler,
    request_queue=queue,
    kv_cache=kv_cache,
    model_runtime=runtime
)


requests = [
    Request(
        request_id="A",
        prompt="Hello",
        max_new_tokens=3
    ),

    Request(
        request_id="B",
        prompt="AI",
        max_new_tokens=5
    ),

    Request(
        request_id="C",
        prompt="GPU",
        max_new_tokens=2
    )
]


for request in requests:
    engine.submit(
        request
    )


iteration = 0


while (
    len(queue) > 0
    or
    len(
        scheduler.active_requests
    ) > 0
):

    iteration += 1

    print(
        f"\nIteration {iteration}"
    )

    outputs = engine.step()

    for request in outputs:

        print(
            request.request_id,
            request.status.value,
            request.generated_tokens
        )