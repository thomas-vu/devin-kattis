def count_paths(N, M, K, colors, edges):
    from collections import defaultdict, deque
    
    graph = defaultdict(list)
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
    
    paths = 0
    for start in range(1, N + 1):
        queue = deque([(start, [start])])
        while queue:
            node, path = queue.popleft()
            if len(path) > 1 and len(set(path)) == len(path):
                paths += 1
            for neighbor in graph[node]:
                if colors[neighbor - 1] not in path:
                    queue.append((neighbor, path + [neighbor]))
    
    return paths

# Read input
N, M, K = map(int, input().split())
colors = list(map(int, input().split()))
edges = [tuple(map(int, input().split())) for _ in range(M)]

# Calculate and output the number of paths
print(count_paths(N, M, K, colors, edges))