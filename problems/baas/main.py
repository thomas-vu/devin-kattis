import sys
from collections import defaultdict, deque

# Read input from stdin
N = int(input())
durations = list(map(int, input().split()))
graph = defaultdict(list)
in_degree = [0] * N
for i in range(N):
    dependencies = list(map(int, input().split()))[1:]
    for dep in dependencies:
        graph[dep - 1].append(i)
        in_degree[i] += 1

# Topological sort using Kahn's algorithm to find the longest path in the DAG
queue = deque([i for i in range(N) if in_degree[i] == 0])
longest_path = [0] * N
while queue:
    node = queue.popleft()
    for neighbor in graph[node]:
        longest_path[neighbor] = max(longest_path[neighbor], longest_path[node] + durations[node])
        in_degree[neighbor] -= 1
        if in_degree[neighbor] == 0:
            queue.append(neighbor)

# Find the step to eliminate to minimize the total time
min_time = float('inf')
for i in range(N):
    # Calculate the time if this step is reduced to 0 seconds
    current_time = sum(durations) - durations[i] + max(longest_path[:i] + longest_path[i+1:])
    min_time = min(min_time, current_time)

# Output the result
print(min_time)