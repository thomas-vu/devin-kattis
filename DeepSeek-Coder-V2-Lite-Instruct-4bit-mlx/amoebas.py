def count_loops(image):
    m, n = len(image), len(image[0])
    loops = 0
    
    def dfs(x, y):
        if x < 0 or x >= m or y < 0 or y >= n or image[x][y] == '.':
            return
        if (x, y) in visited:
            return
        visited.add((x, y))
        
        if x > 0 and image[x-1][y] == '#':
            dfs(x-1, y)
        if x < m-1 and image[x+1][y] == '#':
            dfs(x+1, y)
        if y > 0 and image[x][y-1] == '#':
            dfs(x, y-1)
        if y < n-1 and image[x][y+1] == '#':
            dfs(x, y+1)
    
    for i in range(m):
        for j in range(n):
            if image[i][j] == '#' and (i, j) not in visited:
                if i == 0 or i == m-1 or j == 0 or j == n-1:
                    dfs(i, j)
                else:
                    is_loop = True
                    for dx in [-1, 0, 1]:
                        for dy in [-1, 0, 1]:
                            if dx == 0 and dy == 0:
                                continue
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < m and 0 <= ny < n:
                                if image[nx][ny] == '#':
                                    dfs(nx, ny)
                                else:
                                    is_loop = False
                    if is_loop:
                        loops += 1
    
    return loops

# Read input
m, n = map(int, input().split())
image = [input() for _ in range(m)]
visited = set()
print(count_loops(image))