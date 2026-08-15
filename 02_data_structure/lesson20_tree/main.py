class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

def dfs(node):
    print(node.value)

    for child in node.children:
        dfs(child)

def bfs(node):
    queue = []
    queue.append(node)
    while len(queue) > 0:
        current = queue.pop(0)
        print(current.value)
        for child in current.children:
            queue.append(child)

root = TreeNode("A")

b = TreeNode("B")
c = TreeNode("C")
d = TreeNode("D")

e = TreeNode("E")
f = TreeNode("F")
g = TreeNode("G")

root.children.extend([b,c,d])
b.children.extend([e, f])
d.children.append(g)

dfs(root)

print("--------")

bfs(root)