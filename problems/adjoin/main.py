def find_max_hops(c, l, cables):
    from collections import defaultdict, deque
    
    # Create adjacency list for the graph
    adj_list = defaultdict(list)
    for a, b in cables:
        adj_list[a].append(b)
        adj_list[b].append(a)
    
    # BFS to find the maximum distance from each node
    max_hops = 0
    for i in range(c):
        visited = [False] * c
        queue = deque([i])
        dist = [-1] * c
        dist[i] = 0
        visited[i] = True
        
        while queue:
            node = queue.popleft()
            for neighbor in adj_list[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    dist[neighbor] = dist[node] + 1
                    queue.append(neighbor)
        
        max_hops = max(max_hops, max(dist))
    
    return max_hops

# Read input
c, l = map(int, input().split())
cables = [tuple(map(int, input().split())) for _ in range(l)]

# Output the result
print(find_max_hops(c, l, cables))