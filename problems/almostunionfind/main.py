class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n
        self.size = [1] * n
        self.sums = list(range(n))

    def find(self, p):
        if self.parent[p] != p:
            root = self.find(self.parent[p])
            self.parent[p] = root
        return self.parent[p]

    def union(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        if rootP != rootQ:
            if self.rank[rootP] > self.rank[rootQ]:
                self.parent[rootQ] = rootP
                self.size[rootP] += self.size[rootQ]
                self.sums[rootP] += self.sums[rootQ]
            else:
                self.parent[rootP] = rootQ
                self.size[rootQ] += self.size[rootP]
                self.sums[rootQ] += self.sums[rootP]
                if self.rank[rootP] == self.rank[rootQ]:
                    self.rank[rootQ] += 1

    def move(self, p, q):
        rootP = self.find(p)
        if rootP != self.find(q):
            self.size[rootP] -= 1
            self.sums[rootP] -= p
            self.parent[p] = self.find(q)
            self.size[self.find(q)] += 1
            self.sums[self.find(q)] += p

    def query(self, p):
        rootP = self.find(p)
        return (self.size[rootP], self.sums[rootP])

# Main function to handle input and process commands
def main():
    while True:
        try:
            n, m = map(int, input().split())
            uf = UnionFind(n)
            for _ in range(m):
                cmd = list(map(int, input().split()))
                if cmd[0] == 1:
                    uf.union(cmd[1] - 1, cmd[2] - 1)
                elif cmd[0] == 2:
                    uf.move(cmd[1] - 1, cmd[2] - 1)
                elif cmd[0] == 3:
                    result = uf.query(cmd[1] - 1)
                    print(result[0], result[1])
        except EOFError:
            break

if __name__ == "__main__":
    main()