from collections import defaultdict, deque
import sys

# Read input
n, m = map(int, sys.stdin.readline().split())
edges = defaultdict(list)
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    edges[a].append((b, c))
    edges[b].append((a, c))

# BFS to count single-lane bridges
visited = [False] * (n + 1)
queue = deque([1])
single_lane_count = 0

while queue:
    current = queue.popleft()
    visited[current] = True
    
    for neighbor, bridge_type in edges[current]:
        if not visited[neighbor]:
            queue.append(neighbor)
            if bridge_type == 1:
                single_lane_count += 1

# Output the result
print(single_lane_count)