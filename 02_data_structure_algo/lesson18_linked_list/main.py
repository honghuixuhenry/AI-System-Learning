class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# node1 = Node(10)
# node2 = Node(20)
# node3 = Node(30)

# node1.next = node2
# node2.next = node3

# head = node1

# curent = head
# while curent is not None:
#     print(curent.data)
#     curent = curent.next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def display(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

linked_list = LinkedList()
linked_list.insert_front(10)
linked_list.insert_front(20)
linked_list.insert_front(30)
linked_list.display()
