# This problem can be solved using a graph traversal algorithm and some clever data structures.
# We'll use Breadth-First Search (BFS) to explore the graph and count the number of color changes.
# We'll keep track of the edges in a way that helps us determine the number of color changes for each path.

from collections import deque, defaultdict
import sys

# Read input
N, M = map(int, sys.stdin.readline().split())
edges = defaultdict(list)
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    edges[a].append(b)
    edges[b].append(a)

# BFS to find the shortest path and count color changes
def bfs_color_changes(edges, N):
    queue = deque([(1, -1, 0)])  # (current_node, previous_color, color_changes)
    visited = [False] * (N + 1)
    visited[1] = True
    while queue:
        node, prev_color, color_changes = queue.popleft()
        for neighbor in edges[node]:
            if not visited[neighbor]:
                next_color = 0 if prev_color == 1 else 1
                queue.append((neighbor, next_color, color_changes + (prev_color != next_color)))
                visited[neighbor] = True
    return color_changes - 1 if visited[N] else float('inf')

# Calculate the maximum number of color changes Alice can force on Bob's path from node 1 to node N
max_color_changes = bfs_color_changes(edges, N)
print(max_color_changes)