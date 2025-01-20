def find_path_length(h, w, s, grid):
    start = end = None
    for i in range(h):
        for j in range(w):
            if grid[i][j] == '@':
                start = (i, j)
            elif grid[i][j] == '#':
                end = (i, j)
    
    queue = [(start[0], start[1], 0)]
    visited = set([(start[0], start[1])])
    
    while queue:
        x, y, dist = queue.pop(0)
        
        if (x, y) == end:
            return dist * s
        
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < h and 0 <= ny < w and (nx, ny) not in visited:
                if grid[nx][ny] == '.':
                    queue.append((nx, ny, dist + 1))
                    visited.add((nx, ny))
                elif grid[nx][ny] == '#':
                    queue.append((nx, ny, dist + 1))
                    visited.add((nx, ny))
                elif grid[nx][ny].islower():
                    queue.append((nx, ny, dist + 1))
                    visited.add((nx, ny))
    
    return -1

# Read input
h, w, s = map(int, input().split())
grid = [input() for _ in range(h)]

# Calculate and output the path length
path_length = find_path_length(h, w, s, grid)
print("Your destination will arrive in {} meters".format(path_length))