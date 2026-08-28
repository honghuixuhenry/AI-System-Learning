from queue import Queue
import threading
import time

q = Queue(maxsize=2)

def producer():
    for i in range(5):
        print("Trying to put", i)
        q.put(i)
        print("Added", i)

def consumer():
    while True:
        item = q.get()
        print("Processing:", item)
        time.sleep(3)
        q.task_done()

consumer_thread = threading.Thread(
    target=consumer,
    daemon = True
)

consumer_thread.start()
producer()