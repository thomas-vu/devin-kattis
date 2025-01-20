N, M = 100, 500
import sys
sys.setrecursionlimit(10**6)

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

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
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

# Construct a graph that causes the innermost loop to be visited many times
uf = UnionFind(N)
edges = []
for i in range(1, N):
    uf.union(i, i + 1)
    edges.append((i, i + 1))
for i in range(N - 2):
    uf.union(i + 1, i + 2)
    edges.append((i + 1, i + 2))
for _ in range(M - (N - 1)):
    uf.union(1, 3)
    edges.append((1, 3))

# Output the graph edges
for edge in edges:
    print(edge[0], edge[1])