def min_borders(n, m, image):
    def dfs(x, y, color):
        if (x, y) in visited or image[x][y] != color:
            return 0
        visited.add((x, y))
        count = 1
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                count += dfs(nx, ny, color)
        return count

    visited = set()
    region_sizes = []
    
    for i in range(n):
        for j in range(m):
            if (i, j) not in visited and image[i][j] == '0':
                size = dfs(i, j, '0')
                region_sizes.append(size)
            elif (i, j) not in visited and image[i][j] == '1':
                size = dfs(i, j, '1')
                region_sizes.append(size)
    
    total_pixels = sum(region_sizes)
    min_borders = 0
    
    for size in region_sizes:
        if total_pixels - size < size:
            min_borders += 1
    
    return min_borders

# Read input
n, m = map(int, input().split())
image = [input() for _ in range(n)]

# Output the result
print(min_borders(n, m, image))