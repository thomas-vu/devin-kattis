def find_cars_to_move(m, n, grid, r, c):
    # Directions for moving cars: right and down
    directions = [(0, 1), (1, 0)]
    
    # Find the initial and final positions of cars and empty space
    start = (0, 0)
    end = (r - 1, c - 1)
    
    # Initialize the queue for BFS and visited set
    queue = [(start, [])]
    visited = set()
    
    # BFS to find the sequence of cars to move
    while queue:
        (current, path) = queue.pop(0)
        if current == end:
            return path
        
        (x, y) = current
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n:
                new_grid = [row[:] for row in grid]
                if new_grid[nx][ny] != -1:  # Not empty
                    for i in range(m):
                        for j in range(n):
                            if new_grid[i][j] > 0:
                                new_grid[i][j] -= 1
                    if tuple(map(tuple, new_grid)) not in visited:
                        visited.add(tuple(map(tuple, new_grid)))
                        queue.append(((nx, ny), path + [new_grid[x][y]]))
    
    return "impossible"

# Read input
m, n = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(m)]
r, c = map(int, input().split())

# Output the result
result = find_cars_to_move(m, n, grid, r, c)
print(" ".join(map(str, result)))