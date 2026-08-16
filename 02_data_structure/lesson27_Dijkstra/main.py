import heapq

class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, u, v, weight):
        if u not in self.graph:
            self.add_vertex(u)
        if v not in self.graph:
            self.add_vertex(v)

        self.graph[u].append((v,weight))
        self.graph[v].append((u, weight))

    def dijkstra1(self, start):
        distance = {}

        for vertex in self.graph:
            distance[vertex] = float("inf")

        distance[start] = 0

        heap = []

        heapq.heappush(heap, (0, start))

        while heap:
            current_distance, current_vertex = heapq.heappop(heap)
            if current_distance > distance[current_vertex]:
                continue
            for neighbor, weight in self.graph[current_vertex]:
                new_distance = current_distance + weight
                if new_distance < distance[neighbor]:
                    distance[neighbor] = new_distance
                    heapq.heappush(heap, (new_distance, neighbor))

        return distance

    def dijkstra2(self, start, target):
        distance = {}
        parent = {}

        for vertex in self.graph:
            distance[vertex] = float("inf")

        distance[start] = 0

        heap = []

        heapq.heappush(heap, (0, start))

        while heap:
            current_distance, current_vertex = heapq.heappop(heap)
            if current_distance > distance[current_vertex]:
                continue
            if current_vertex == target:
                break
            for neighbor, weight in self.graph[current_vertex]:
                new_distance = current_distance + weight
                if new_distance < distance[neighbor]:
                    distance[neighbor] = new_distance
                    parent[neighbor] = current_vertex
                    heapq.heappush(heap, (new_distance, neighbor))

        if target not in parent and target!= start:
            return None

        path = []
        current = target
        while current!= start:
            path.append(current)
            current = parent[current]

        path.append(start)
        path.reverse()

        return path, distance[target]
    
g = Graph()

g.add_edge("A", "B", 10)
g.add_edge("A", "C", 2)
g.add_edge("C", "D", 2)
g.add_edge("D", "B", 2)

print(g.dijkstra2("A", "B"))