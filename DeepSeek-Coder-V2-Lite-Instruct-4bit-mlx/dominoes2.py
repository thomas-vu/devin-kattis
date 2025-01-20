class DominoesFallen:
    def __init__(self, n, edges, knocked_over):
        self.n = n
        self.edges = edges
        self.knocked_over = knocked_over
        self.graph = [[] for _ in range(n + 1)]
        for x, y in edges:
            self.graph[x].append(y)
        self.visited = [False] * (n + 1)
    
    def dfs(self, node):
        if self.visited[node]:
            return
        self.visited[node] = True
        for neighbor in self.graph[node]:
            self.dfs(neighbor)
    
    def count_fallen_dominoes(self):
        for domino in self.knocked_over:
            if not self.visited[domino]:
                self.dfs(domino)
        return sum(self.visited[1:])

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    test_cases = int(data[index])
    index += 1
    results = []
    
    for _ in range(test_cases):
        n = int(data[index])
        m = int(data[index + 1])
        l = int(data[index + 2])
        index += 3
        
        edges = []
        for _ in range(m):
            x = int(data[index])
            y = int(data[index + 1])
            edges.append((x, y))
            index += 2
        
        knocked_over = []
        for _ in range(l):
            z = int(data[index])
            knocked_over.append(z)
            index += 1
        
        dominoes = DominoesFallen(n, edges, knocked_over)
        results.append(dominoes.count_fallen_dominoes())
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()