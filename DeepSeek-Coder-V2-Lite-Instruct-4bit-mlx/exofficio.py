import sys
from collections import deque

def bfs(grid, R, C):
    dist = [[float('inf')] * (C + 2) for _ in range(R + 2)]
    queue = deque()
    
    for r in range(1, R + 1):
        for c in range(1, C + 2, 2):
            queue.append((r, c))
            dist[r][c] = 0
    
    while queue:
        r, c = queue.popleft()
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 1 <= nr <= R and 1 <= nc <= C + 1:
                if dist[nr][nc] == float('inf'):
                    dist[nr][nc] = dist[r][c] + 1
                    queue.append((nr, nc))
    
    return dist

R, C = map(int, sys.stdin.readline().split())
grid = [[0] * (C + 2) for _ in range(R + 2)]

for r in range(1, R + 1):
    for c in range(1, C + 2, 2):
        grid[r][c] = 1
for c in range(1, C + 2):
    for r in range(1, R + 1, 2):
        grid[r][c] = 1

dist = bfs(grid, R, C)
max_dist = max([max(row) for row in dist])

# Build walls to minimize the maximum gathering time
for r in range(1, R + 1):
    for c in range(2, C + 1, 2):
        if dist[r][c] == max_dist:
            grid[r][c] = 1
        else:
            grid[r + 1][c] = 1

# Output the result
for r in range(R + 1):
    for c in range(C + 2):
        if r == 0 and c % 2 == 0:
            sys.stdout.write('_')
        elif r == R and c % 2 == 0:
            sys.stdout.write('_')
        elif r < R and c % 2 == 0:
            if grid[r][c // 2] and grid[r + 1][c // 2]:
                sys.stdout.write('|')
            else:
                sys.stdout.write('_')
        elif r == 0 and c % 2 != 0:
            sys.stdout.write(' ')
        elif r == R and c % 2 != 0:
            sys.stdout.write(' ')
        elif r < R and c % 2 != 0:
            if grid[r][(c + 1) // 2] and grid[r][(c - 1) // 2]:
                sys.stdout.write('|')
            else:
                sys.stdout.write('_')
    sys.stdout.write('\n')