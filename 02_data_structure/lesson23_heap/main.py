import heapq

# heap = []

# heapq.heappush(heap, 5)
# heapq.heappush(heap, 2)
# heapq.heappush(heap, 8)
# heapq.heappush(heap, 1)

# print(heap)

# smallest = heapq.heappop(heap)
# print(smallest)

# heapq.heappush(heap,0)
# print(heap)

class PriorityQueue:
    def __init__(self):
        self.items = []

    def push(self, priority):
        heapq.heappush(self.items, priority)

    def pop(self):
        return heapq.heappop(self.items)

    def peek(self):
        return self.items[0]

    def is_empty(self):
        if len(self.items) == 0:
            return True
        else:
            return False

    def size(self):
        return len(self.items)

PQ = PriorityQueue()
PQ.push((2,"Download"))
PQ.push((3, "Emergency"))
PQ.push((6, "KSU"))
PQ.push((4, "Honghui"))
PQ.push((1, "Marietta"))

print(PQ.items)
print(PQ.peek())

print(PQ.pop())

print(PQ.items)
print(PQ.peek())

print(PQ.is_empty())
print(PQ.size())