def read_ints():
    return list(map(int, input().split()))

# Read inputs
A, F = read_ints()
L, W = read_ints()
grid = [input().strip() for _ in range(L)]

# Find positions of 'S' and 'G'
start = None
goal = None
for i in range(L):
    for j in range(W):
        if grid[i][j] == 'S':
            start = (i, j)
        elif grid[i][j] == 'G':
            goal = (i, j)

# Helper function to check if a position is within the grid
def in_grid(x, y):
    return 0 <= x < L and 0 <= y < W

# BFS to find the shortest path from a start position
def bfs(start_pos):
    queue = [start_pos]
    visited = set([start_pos])
    distance = {start_pos: 0}
    
    while queue:
        x, y = queue.pop(0)
        if (x, y) == goal:
            return distance[(x, y)]
        
        for dx in range(-F, F + 1):
            for dy in range(-F, F + 1):
                nx, ny = x + dx, y + dy
                if in_grid(nx, ny) and (nx, ny) not in visited and grid[nx][ny] == 'W':
                    visited.add((nx, ny))
                    distance[(nx, ny)] = distance[(x, y)] + 1
                    queue.append((nx, ny))
    
    return float('inf')

# Calculate distances for Elsa and the father
elisa_dist = bfs(start)
father_dist = bfs(start)

# Determine the outcome
if elisa_dist == float('inf') and father_dist == float('inf'):
    print("NO WAY")
elif elisa_dist <= father_dist:
    if elisa_dist == father_dist:
        print("SUCCESS")
    else:
        print("GO FOR IT")
else:
    print("NO CHANCE")