class UnionFind:
    def __init__(self):
        self.parent = {}
        self.rank = {}

    def make_set(self, x):
        self.parent[x] = x
        self.rank[x] = 0

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if self.rank[rootX] < self.rank[rootY]:
            self.parent[rootX] = rootY
        elif self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX
        else:
            self.parent[rootY] = rootX
            self.rank[rootX] += 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)

uf = UnionFind()

uf.make_set("A")
uf.make_set("B")
uf.make_set("C")
uf.make_set("D")

uf.union("A","B")
uf.union("B","C")
uf.union("C","D")

print(uf.parent)

print(uf.find("C"))

print(uf.parent)

print(uf.find("B"))

print(uf.parent)

print(uf.connected("B","C"))