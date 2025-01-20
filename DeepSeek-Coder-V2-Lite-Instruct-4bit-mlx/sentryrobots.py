def min_robots(grid, points, obstacles):
    # Helper function to check if a point is in the grid
    def is_valid(y, x):
        return 0 <= y < len(grid) and 0 <= x < len(grid[0])
    
    # Create a new grid to mark points and obstacles
    for wy, wx in obstacles:
        grid[wy - 1][wx - 1] = '#'
    for py, px in points:
        grid[py - 1][px - 1] = '*'
    
    # Count the number of robots needed
    count = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == '*':
                # Check all four directions from each point of interest
                if is_valid(y - 1, x) and grid[y - 1][x] != '#' and grid[y - 1][x] != '*':
                    continue
                if is_valid(y + 1, x) and grid[y + 1][x] != '#' and grid[y + 1][x] != '*':
                    continue
                if is_valid(y, x - 1) and grid[y][x - 1] != '#' and grid[y][x - 1] != '*':
                    continue
                if is_valid(y, x + 1) and grid[y][x + 1] != '#' and grid[y][x + 1] != '*':
                    continue
                count += 1
    return count

# Read the input
import sys
input = sys.stdin.read
lines = input().split('\n')
index = 0
C = int(lines[index].strip())
index += 1
for _ in range(C):
    index += 1  # Skip the empty line
    Y, X = map(int, lines[index].strip().split())
    index += 1
    P = int(lines[index].strip())
    points = []
    for _ in range(P):
        index += 1
        py, px = map(int, lines[index].strip().split())
        points.append((py, px))
    W = int(lines[index].strip())
    obstacles = []
    for _ in range(W):
        index += 1
        wy, wx = map(int, lines[index].strip().split())
        obstacles.append((wy, wx))
    index += 1
    
    # Create the grid and solve each case
    grid = [['.' for _ in range(X)] for _ in range(Y)]
    print(min_robots(grid, points, obstacles))