def can_form_spanning_tree_with_k_blue_edges(n, m, k, edges):
    from collections import defaultdict, deque
    
    graph = defaultdict(list)
    for edge in edges:
        c, f, t = edge
        graph[f].append((t, 1 if c == 'B' else 0))
        graph[t].append((f, 1 if c == 'B' else 0))
    
    visited = [False] * (n + 1)
    blue_edges = 0
    
    def bfs(start):
        nonlocal blue_edges
        queue = deque([start])
        visited[start] = True
        
        while queue:
            node = queue.popleft()
            for neighbor, color in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
                    if color == 1:
                        blue_edges += 1
    
    bfs(1)
    
    return 1 if blue_edges == k else 0

# Read input
n, m, k = map(int, input().split())
edges = []
for _ in range(m):
    c, f, t = input().split()
    edges.append((c, int(f), int(t)))

# Output the result
print(can_form_spanning_tree_with_k_blue_edges(n, m, k, edges))