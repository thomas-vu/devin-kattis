def bfs(grid, start):
    R = len(grid)
    C = len(grid[0])
    visited = [[False] * C for _ in range(R)]
    queue = [start]
    visited[start[0]][start[1]] = True
    count = 0
    
    while queue:
        x, y = queue.pop(0)
        count += 1
        
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny] and grid[nx][ny] == '#':
                visited[nx][ny] = True
                queue.append((nx, ny))
    
    return count

R = int(input())
C = int(input())
U = int(input())
grid = [list(input().strip()) for _ in range(R)]
stockholm = None

for i in range(R):
    for j in range(C):
        if grid[i][j] == 'S':
            stockholm = (i, j)
            break
    if stockholm is not None:
        break

initial_landmass = bfs(grid, stockholm)
print(initial_landmass)

for _ in range(U):
    i, j = map(int, input().split())
    grid[i-1][j-1] = '#'
    new_landmass = bfs(grid, stockholm)
    print(new_landmass)