# stack = []

# stack.append(10)
# stack.append(20)
# stack.append(30)

# print(stack)

# stack.pop()
# print(stack)

# stack = []

# stack.append("A")
# stack.append("B")
# stack.append("C")

# print(stack[-1])
# print(stack)

# print(stack.pop())

# print(stack)

# print(stack.pop())

# print(stack)

# print(stack.pop())

# print(stack)

# def A():
#     B()

# def B():
#     C()

# def C():
#     print("Hello World")

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def clear(self):
        self.items = []

    def display(self):
        print(self.items)
    

stack = Stack()

print(stack.is_empty())
stack.push(10)
stack.push(20)
stack.push(30)

print(stack.peek())
print(stack.size())
print(stack.pop())
print(stack.peek())
print(stack.size())
# stack.clear()
# print(stack.is_empty())

stack.display()