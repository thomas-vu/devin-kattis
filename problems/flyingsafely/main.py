def min_pilots_to_trust(n, flights):
    graph = {i: set() for i in range(1, n + 1)}
    for a, b in flights:
        graph[a].add(b)
        graph[b].add(a)
    
    visited = set()
    def dfs(node):
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                dfs(neighbor)
    
    count = 0
    for node in range(1, n + 1):
        if node not in visited:
            dfs(node)
            count += 1
    
    return count

def main():
    t = int(input())
    results = []
    for _ in range(t):
        n, m = map(int, input().split())
        flights = [tuple(map(int, input().split())) for _ in range(m)]
        result = min_pilots_to_trust(n, flights)
        results.append(result)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()