import sys
from collections import deque

# Read input
n, k = map(int, sys.stdin.readline().split())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# Directions for the 4 possible moves (up, down, left, right)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# Find the positions of all tiles numbered from 1 to k
positions = {}
for i in range(n):
    for j in range(n):
        num = matrix[i][j]
        if num <= k:
            positions[num] = (i, j)

# BFS to find the shortest path between each pair of consecutive tiles
distances = [[float('inf')] * (k + 1) for _ in range(k + 1)]
for start in range(1, k):
    if start not in positions:
        continue
    queue = deque([(positions[start], 0)])
    visited = [[False] * n for _ in range(n)]
    visited[positions[start][0]][positions[start][1]] = True
    while queue:
        (x, y), d = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                visited[nx][ny] = True
                next_num = matrix[nx][ny]
                if next_num > start and next_num <= k:
                    distances[start][next_num] = d + 1
                    queue.append(((nx, ny), d + 1))

# Calculate the shortest path for the entire game of Hopscotch
if k == 1:
    print(0)
else:
    min_distance = float('inf')
    for i in range(1, k):
        if distances[1][i] == float('inf'):
            min_distance = -1
            break
    if min_distance == float('inf'):
        for i in range(2, k + 1):
            if distances[i - 1][i] == float('inf'):
                min_distance = -1
                break
            else:
                min_distance = min(min_distance, distances[i - 1][i])
    if min_distance != float('inf'):
        print(min_distance)
    else:
        print(-1)