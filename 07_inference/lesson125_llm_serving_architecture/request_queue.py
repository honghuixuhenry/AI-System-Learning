from collections import deque


class RequestQueue:

    def __init__(self):
        self._queue = deque()


    def push(self, request):
        self._queue.append(request)


    def pop(self):
        if not self._queue:
            return None

        return self._queue.popleft()


    def __len__(self):
        return len(self._queue)

queue = RequestQueue()

queue.push({
    "id": "A",
    "prompt": "Hello"
})

queue.push({
    "id": "B",
    "prompt": "Explain transformers"
})

print(len(queue))