# with open("test.txt" "r") as file:
#     content = file.read()

class MyContect:
    def __enter__(self):
        print("Enter")
        return self
    def __exit__(self, exc_type, exc, tb):
        print("Exit")

with MyContect():
    print("Working")

import time

class Timer:
    def __enter__(self):
        self.start = time.time()
        return self
    def __exit__(self, exc_type, exc, tb):
        end = time.time()
        print(f"Elapsed: {end-self.start:.4f}s")

with Timer():
    total = 0
    for i in range(1000000):
        total += i

