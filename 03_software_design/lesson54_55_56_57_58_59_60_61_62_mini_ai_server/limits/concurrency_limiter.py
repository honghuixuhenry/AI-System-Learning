import threading 
import time

semaphore = threading.Semaphore(2)

def task(name):
    with semaphore:
        print(name, "start")
        time.sleep(3)
        print(name, "end")

threads = []

for i in range(5):
    t = threading.Thread(
        target=task,
        args=(f"Task {i}",)
    )

    threads.append(t)
    t.start()

for t in threads:
    t.join()

import asyncio 

semaphore = asyncio.Semaphore(2)

async def task(name):
    async with semaphore:
        print(name, "start")
        await asyncio.sleep(3)
        print(name, "end")

async def main():
    await asyncio.gather(
        task("A"),
        task("B"),
        task("C"),
        task("D"),
        task("E")
    )
asyncio.run(main())

import time 

class RateLimiter:
    def __init__(self, max_requests, window):
        self.max_requests = max_requests
        self.window = window
        self.requests = []

    def allow(self):
        now = time.time()
        self.requests = [
            t for t in self.requests
            if now - t < self.window
        ]
        if len(self.requests) >= self.max_requests:
            return False
        self.requests.append(now)
        return True

limiter = RateLimiter(
    max_requests=5,
    window=60
)

if limiter.allow():
    print("Accepted")
else:
    print("Too many requests")
    