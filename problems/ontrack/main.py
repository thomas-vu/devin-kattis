import sys
from collections import defaultdict, deque

def read_ints():
    return list(map(int, sys.stdin.readline().strip().split()))

n = int(sys.stdin.readline().strip())
edges = defaultdict(list)
for _ in range(n):
    u, v = read_ints()
    edges[u].append(v)
    edges[v].append(u)

# Find the critical junction that disconnects the most pairs of junctions
def find_critical_junction(edges, n):
    critical_junction = -1
    max_disconnections = -1
    
    for junction in range(n):
        visited = [False] * n
        queue = deque([junction])
        disconnections = 0
        
        while queue:
            node = queue.popleft()
            visited[node] = True
            
            for neighbor in edges[node]:
                if not visited[neighbor]:
                    queue.append(neighbor)
                else:
                    disconnections += 1
        
        if disconnections > max_disconnections:
            max_disconnections = disconnections
            critical_junction = junction
    
    return critical_junction

critical_junction = find_critical_junction(edges, n)

# Calculate the number of disconnected pairs before and after adding a new rail line
def count_disconnected_pairs(edges, n, critical_junction):
    visited = [False] * n
    queue = deque([critical_junction])
    
    while queue:
        node = queue.popleft()
        visited[node] = True
        
        for neighbor in edges[node]:
            if not visited[neighbor]:
                queue.append(neighbor)
    
    # Count pairs of junctions that are not visited (disconnected)
    disconnected_count = 0
    for i in range(n):
        if not visited[i]:
            for j in range(i + 1, n):
                if not visited[j]:
                    disconnected_count += 1
    
    return disconnected_count

# Add a new rail line to minimize the number of disconnected pairs
def add_new_rail_line(edges, n):
    min_disconnections = float('inf')
    best_pair = (-1, -1)
    
    for u in range(n):
        for v in edges[u]:
            if u not in edges[v]:  # Ensure the new line is added between unconnected junctions
                edges[u].append(v)
                edges[v].append(u)
                
                disconnections = count_disconnected_pairs(edges, n, critical_junction)
                if disconnections < min_disconnections:
                    min_disconnections = disconnections
                    best_pair = (u, v)
                
                edges[u].remove(v)
                edges[v].remove(u)
    
    return best_pair

# Output the results
best_pair = add_new_rail_line(edges, n)
n1 = count_disconnected_pairs(edges, n, critical_junction)
n2 = min_disconnections

print(f"{n1} {n2}")