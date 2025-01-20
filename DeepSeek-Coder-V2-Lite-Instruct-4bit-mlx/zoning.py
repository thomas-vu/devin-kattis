import sys
from collections import deque

# Read input
n = int(input().strip())
grid = []
for _ in range(n):
    grid.append(list(map(int, input().strip())))

# Directions for moving in the grid (N, E, S, W)
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# Helper function to check if a position is within the grid
def is_valid(x, y):
    return 0 <= x < n and 0 <= y < n

# Function to find the shortest distance from a residential zone to any commercial zone using BFS
def bfs(start_x, start_y):
    visited = [[False] * n for _ in range(n)]
    queue = deque([(start_x, start_y, 0)])  # (x, y, distance)
    visited[start_x][start_y] = True
    min_distance = float('inf')
    
    while queue:
        x, y, dist = queue.popleft()
        
        if grid[x][y] == 3:
            min_distance = min(min_distance, dist)
            continue
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny) and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, dist + 1))
    
    return min_distance

# Main logic to find the maximum distance from a residential zone to the closest commercial zone
max_distance = 0
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:  # Residential zone
            min_dist = bfs(i, j)
            max_distance = max(max_distance, min_dist)

# Output the result
print(max_distance)