# Read input
N, M = map(int, input().split())
bridges = [list(map(int, input().split())) for _ in range(M)]
armies = [int(input()) for _ in range(N)]

# Create adjacency list
adj_list = [[] for _ in range(N + 1)]
for u, v in bridges:
    adj_list[u].append(v)
    adj_list[v].append(u)

# Union-Find data structure for tracking connected components
class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size
        self.size = [1] * size  # Size of each component

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
                self.size[rootX] += self.size[rootY]
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
                self.size[rootY] += self.size[rootX]
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1
                self.size[rootX] += self.size[rootY]

# Initialize UnionFind and process each bridge
uf = UnionFind(N + 1)
for i in range(N):
    for neighbor in adj_list[i + 1]:
        if armies[neighbor - 1] < armies[i]:
            uf.union(neighbor, i + 1)

# Find the maximum army size of the Spanning Nation
max_army = 0
for i in range(N):
    if uf.find(i + 1) == uf.find(1):
        max_army = max(max_army, armies[i])

# Output the result
print(max_army)