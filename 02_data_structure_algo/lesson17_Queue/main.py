# from collections import deque

# queue = deque()

# queue.append(10)
# queue.append(20)
# queue.append(30)

# print(queue.popleft())

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[0]
    
    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def display(self):
        print(self.items)

queue = Queue()
queue.enqueue("A")
queue.enqueue("B")
queue.enqueue("C")

print(queue.peek())
print(queue.dequeue())
print(queue.peek())
print(queue.size())
queue.display()