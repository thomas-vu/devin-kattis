def max_distance(grid):
    n = len(grid)
    distances = [[float('inf')] * n for _ in range(n)]
    
    from collections import deque
    
    queue = deque()
    
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 'S':
                distances[i][j] = 0
                queue.append((i, j))
            elif grid[i][j] == 'H':
                distances[i][j] = float('inf')
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    while queue:
        x, y = queue.popleft()
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < n and 0 <= ny < n:
                if grid[nx][ny] == '.' and distances[x][y] + 1 < distances[nx][ny]:
                    distances[nx][ny] = distances[x][y] + 1
                    queue.append((nx, ny))
    
    max_dist = -float('inf')
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 'S':
                max_dist = max(max_dist, distances[i][j])
    
    return max_dist

# Read input
N = int(input())
grid = [list(input().strip()) for _ in range(N)]

# Output the result
print(max_distance(grid))