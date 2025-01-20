import sys

# Helper function to check if the current position is valid and not visited
def is_valid(x, y):
    return 0 <= x < n and 0 <= y < m and not visited[x][y]

# Helper function to find the exit from the maze
def find_exit(start_x, start_y):
    stack = [(start_x, start_y)]
    visited[start_x][start_y] = True
    
    while stack:
        cx, cy = stack.pop()
        
        # Check all four possible directions
        if cx == n - 1 and cy == m - 1:
            return True
        
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = cx + dx, cy + dy
            
            if is_valid(nx, ny) and maze[nx][ny] != 'wall':
                stack.append((nx, ny))
                visited[nx][ny] = True
    
    return False

# Read the size of the maze
n, m = map(int, sys.stdin.readline().split())

# Initialize the maze and visited array
maze = []
for _ in range(n):
    row = list(sys.stdin.readline().strip())
    maze.append(row)

# Initialize the visited array
visited = [[False] * m for _ in range(n)]

# Start from the top-left corner of the maze
start_x, start_y = 0, 0

# Find the exit from the maze
if find_exit(start_x, start_y):
    print("solved")
else:
    print("no way out")