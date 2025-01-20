def count_routes(N, M, roads):
    from collections import defaultdict, deque
    
    if N == 1:
        return 0
    
    graph = defaultdict(list)
    for A, B in roads:
        graph[A].append(B)
    
    # Use BFS to count the number of ways from town 1 to town N
    queue = deque([(1, 0)])  # (current_town, path_count)
    visited = [False] * (N + 1)
    visited[1] = True
    path_count = [0] * (N + 1)
    path_count[1] = 1
    
    while queue:
        current, count = queue.popleft()
        
        for next_town in graph[current]:
            if not visited[next_town]:
                visited[next_town] = True
                queue.append((next_town, count + 1))
            path_count[next_town] += path_count[current]
    
    return path_count[2] % 1000000000 if path_count[2] < 1000000000 else "inf"

# Read input
import sys
input = sys.stdin.read
data = input().split()
N, M = int(data[0]), int(data[1])
roads = [(int(data[2*i+2]), int(data[2*i+3])) for i in range(M)]

# Get the number of routes
result = count_routes(N, M, roads)
print(result)