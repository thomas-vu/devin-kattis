import sys
from collections import deque

# Read input
N = int(input())
heights = []
growth_speeds = []
for _ in range(N):
    heights.append(list(map(int, input().split())))
for _ in range(N):
    growth_speeds.append(list(map(int, input().split())))

# Calculate future heights after one year for each tree
future_heights = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        future_heights[i][j] = heights[i][j] + growth_speeds[i][j]

# DFS to find connected components of trees with the same height after one year
def dfs(x, y):
    stack = [(x, y)]
    while stack:
        cx, cy = stack.pop()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < N and 0 <= ny < N and future_heights[nx][ny] == future_heights[x][y]:
                stack.append((nx, ny))
    return 1

# Count connected components of trees with the same height after one year
visited = [[False] * N for _ in range(N)]
components_count = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            components_count += dfs(i, j)

# Output the result
print(components_count)