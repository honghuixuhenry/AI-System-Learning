from collections import deque


class RequestQueue:

    def __init__(self):
        self._queue = deque()

    def push(self, request):
        self._queue.append(
            request
        )

    def pop(self):
        if not self._queue:
            return None

        return self._queue.popleft()

    def empty(self):
        return len(
            self._queue
        ) == 0

    def __len__(self):
        return len(
            self._queue
        )