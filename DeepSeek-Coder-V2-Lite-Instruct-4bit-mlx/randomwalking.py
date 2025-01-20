def is_good_graph(k, n, edges):
    from collections import defaultdict, deque
    
    # Build adjacency list for the graph
    adj_list = defaultdict(list)
    for v1, v2 in edges:
        adj_list[v1].append(v2)
        adj_list[v2].append(v1)
    
    # Perform BFS to simulate the random walk
    def bfs(start):
        visited = set()
        queue = deque([start])
        bit_counts = [0] * n
        
        while queue and len(visited) < 2**n:
            node = queue.popleft()
            if node not in visited:
                visited.add(node)
                for bit_index in range(n):
                    if node & (1 << bit_index):
                        bit_counts[bit_index] += 1
                for neighbor in adj_list[node]:
                    if neighbor not in visited:
                        queue.append(neighbor)
        
        # Check the probability of each bit being 1
        for count in bit_counts:
            if not (25 < count * 100 / len(visited) < 75):
                return False
        return True
    
    # Check each node as a starting point
    for start in range(2**n):
        if not bfs(start):
            return False
    return True

# Main loop to process input
while True:
    k, n, e = map(int, input().split())
    if k == 0 and n == 0 and e == 0:
        break
    
    edges = [tuple(map(int, input().split())) for _ in range(e)]
    
    if is_good_graph(k, n, edges):
        print("Yes")
    else:
        print("No")