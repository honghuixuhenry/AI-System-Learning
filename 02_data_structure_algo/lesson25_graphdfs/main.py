# graph = {
#     "A": ["B", "C"],
#     "B": ["A", "C", "D"],
#     "C": ["A", "B", "D"],
#     "D": ["B", "C"]
# }


class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, u, v):
        if u not in self.graph:
            self.add_vertex(u)
        if v not in self.graph:
            self.add_vertex(v)
        self.graph[u].append(v)
        self.graph[v].append(u)

    def remove_vertex(self, vertex):
        if vertex in self.graph:
            for neighbor in self.graph[vertex]:
                 self.graph[neighbor].remove(vertex)
            del self.graph[vertex]

    def remove_edge(self, u, v):
        if u in self.graph and v in self.graph[u]:
            self.graph[u].remove(v)
        if v in self.graph and u in self.graph[v]:
            self.graph[v].remove(u)

    def has_edge(self, u, v):
        if u not in self.graph:
            return False
        else:
            if v in self.graph[u]:
                return True
            else: 
                return False

    def display(self):
        for vertex, neighbors in self.graph.items():
            print(vertex, "-->", neighbors)

    def dfs(self, start):
        visited = set()
        self._dfs(start, visited)

    def _dfs(self, vertex, visited):
        if vertex in visited:
            return
        visited.add(vertex)
        print(vertex)
        for neighbors in self.graph[vertex]:
            self._dfs(neighbors, visited)
        # print(vertex)

g = Graph()
g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_vertex("D")
g.add_edge("A","B")
g.add_edge("A","C")
g.add_edge("B","D")
g.add_edge("C","D")
g.display()

print(g.dfs("A"))