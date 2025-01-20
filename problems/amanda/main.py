def min_lounges(n, m, routes):
    from collections import defaultdict, deque
    
    graph = defaultdict(list)
    in_degree = [0] * (n + 1)
    out_degree = [0] * (n + 1)
    
    for a, b, c in routes:
        graph[a].append((b, c))
        out_degree[a] += 1
        in_degree[b] += 1
    
    def is_possible(start):
        visited = [False] * (n + 1)
        stack = deque([start])
        visited[start] = True
        count = 0
        
        while stack:
            node = stack.popleft()
            count += 1
            for neighbor, c in graph[node]:
                if not visited[neighbor] and (c == 1 or c == 2):
                    visited[neighbor] = True
                    stack.append(neighbor)
        
        return count == n
    
    start_node = 1
    while not is_possible(start_node):
        start_node += 1
    
    lounges = [0] * (n + 1)
    for a, b, c in routes:
        if c == 2:
            lounges[a] = 1
            lounges[b] = 1
        elif c == 1:
            if out_degree[a] > in_degree[a]:
                lounges[a] = 1
            else:
                lounges[b] = 1
    
    return sum(lounges)

# Read input
n, m = map(int, input().split())
routes = [list(map(int, input().split())) for _ in range(m)]

# Output the result
result = min_lounges(n, m, routes)
if result == float('inf'):
    print("impossible")
else:
    print(result)