import math
from collections import deque

def shortest_path(n, k):
    if n == 1:
        return 0
    
    visited = set()
    queue = deque([(0, 0)])  # (current_node, distance)
    
    while queue:
        current_node, dist = queue.popleft()
        
        # Check all possible next nodes
        for next_node in range(max(0, current_node - k + 1), min(n, current_node + k)):
            if next_node not in visited:
                visited.add(next_node)
                queue.append((next_node, dist + 1))
                if next_node == n - 1:
                    return dist + 1
    
    return -1

# Read input
n, k = map(int, input().split())

# Calculate and print the shortest path
print(shortest_path(n, k))