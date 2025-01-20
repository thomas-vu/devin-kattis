def main():
    n, m, c = map(int, input().split())
    roads = [list(map(int, input().split())) for _ in range(m)]
    starts = list(map(int, input().split()))
    
    # Build the graph from the roads
    graph = {i: [] for i in range(1, n + 1)}
    for x, y, t in roads:
        graph[x].append((y, t))
        graph[y].append((x, t))
    
    # Use a modified DFS to count the maximum number of commuters
    def dfs(start, visited):
        stack = [(start, 0)]
        count = 0
        while stack:
            node, time = stack.pop()
            if node == 1 and time <= min_time:
                count += 1
            else:
                for neighbor, edge_time in graph[node]:
                    if (neighbor, edge_time) not in visited:
                        visited.add((neighbor, edge_time))
                        stack.append((neighbor, time + edge_time))
        return count
    
    max_count = 0
    for start in starts:
        visited = set()
        min_time = float('inf')
        # Find the minimum time to reach downtown from each start point
        for neighbor, edge_time in graph[start]:
            min_time = min(min_time, edge_time)
        # Use DFS to count the number of commuters that can reach downtown without congestion
        max_count = max(max_count, dfs(start, visited))
    
    print(max_count)

if __name__ == "__main__":
    main()