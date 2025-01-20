class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
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

n = int(input())
uf = UnionFind(0)
building_index = {}
index = 0

for _ in range(n):
    a, b = input().split()
    if a not in building_index:
        building_index[a] = index
        index += 1
    if b not in building_index:
        building_index[b] = index
        index += 1
    uf.union(building_index[a], building_index[b])
    print(uf.get_size(building_index[a]))