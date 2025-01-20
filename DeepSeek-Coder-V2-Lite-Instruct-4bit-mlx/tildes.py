class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n
        self.size = [1] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
                self.size[root_u] += self.size[root_v]
            else:
                self.parent[root_u] = root_v
                self.size[root_v] += self.size[root_u]
                if self.rank[root_u] == self.rank[root_v]:
                    self.rank[root_v] += 1

    def get_size(self, u):
        return self.size[self.find(u)]

n, q = map(int, input().split())
uf = UnionFind(n)

for _ in range(q):
    query = input().split()
    if query[0] == 't':
        a, b = int(query[1]) - 1, int(query[2]) - 1
        uf.union(a, b)
    elif query[0] == 's':
        a = int(query[1]) - 1
        print(uf.get_size(a))