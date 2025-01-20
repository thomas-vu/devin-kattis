def main():
    N = int(input())
    islands = []
    
    for _ in range(N):
        line = list(map(int, input().split()))
        Ti = line[0]
        Ki = line[1]
        islands.append((Ti, Ki, list(zip(line[2:Ki*2+2:2], line[3:Ki*2+2:2]))))
    
    def dfs(node, visited):
        if node in visited:
            return 0
        visited.add(node)
        _, _, edges = islands[node-1]
        for edge in edges:
            dfs(edge[0], visited)
        return 1
    
    visited = set()
    survivors = N - dfs(1, visited)
    print(survivors)

if __name__ == "__main__":
    main()