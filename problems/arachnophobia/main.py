import sys
from collections import defaultdict, deque

# Read input from stdin
N, M, T = map(int, sys.stdin.readline().split())
edges = defaultdict(list)
for _ in range(M):
    u, v, d = map(int, sys.stdin.readline().split())
    edges[u].append((v, d))
    edges[v].append((u, d))
s, t = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline().split()[0])
spider_locations = list(map(int, sys.stdin.readline().split()))

# Perform BFS to find the shortest path from s to all other nodes
dist = [float('inf')] * N
dist[s] = 0
queue = deque([s])
while queue:
    node = queue.popleft()
    for neighbor, weight in edges[node]:
        if dist[neighbor] > dist[node] + weight:
            dist[neighbor] = dist[node] + weight
            queue.append(neighbor)

# Perform another BFS from t to find the maximum D for each node on the path to t
max_D = [0] * N
queue = deque([t])
while queue:
    node = queue.popleft()
    for neighbor, weight in edges[node]:
        if dist[neighbor] < dist[node] - weight:
            continue
        min_dist = float('inf')
        for spider in spider_locations:
            min_dist = min(min_dist, abs(neighbor - spider))
        max_D[neighbor] = max(max_D[neighbor], min_dist)
        queue.append(neighbor)

# The answer is the maximum D on the path from s to t in no more than T seconds
# We need to find the maximum D on the path from s to t considering the spiders
answer = 0
for i in range(N):
    if dist[i] <= T:
        min_dist = float('inf')
        for spider in spider_locations:
            min_dist = min(min_dist, abs(i - spider))
        answer = max(answer, min_dist)

# Output the result
print(answer)