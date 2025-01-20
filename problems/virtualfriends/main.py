from collections import defaultdict

class UnionFind:
    def __init__(self):
        self.parent = {}
        self.rank = {}
        self.size = defaultdict(int)
    
    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 0
            self.size[x] = 1
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
                self.size[rootX] += self.size[rootY]
            else:
                self.parent[rootX] = rootY
                self.size[rootY] += self.size[rootX]
                if self.rank[rootX] == self.rank[rootY]:
                    self.rank[rootY] += 1
    
    def getSize(self, x):
        rootX = self.find(x)
        return self.size[rootX]

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    T = int(data[index])
    index += 1
    uf = UnionFind()
    
    for _ in range(T):
        F = int(data[index])
        index += 1
        for _ in range(F):
            x = data[index]
            y = data[index + 1]
            index += 2
            uf.union(x, y)
            print(uf.getSize(x))

if __name__ == "__main__":
    main()