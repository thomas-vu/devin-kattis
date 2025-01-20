def fill_rings(grid, n, m):
    ring = [[0] * m for _ in range(n)]
    
    def is_valid(x, y):
        return 0 <= x < n and 0 <= y < m and grid[x][y] == 'T'
    
    def assign_rings(x, y, ring_num):
        queue = [(x, y)]
        while queue:
            cx, cy = queue.pop(0)
            if is_valid(cx, cy) and ring[cx][cy] == 0:
                ring[cx][cy] = ring_num
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = cx + dx, cy + dy
                    if is_valid(nx, ny):
                        queue.append((nx, ny))
    
    ring_num = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'T' and ring[i][j] == 0:
                assign_rings(i, j, ring_num)
                ring_num += 1
    
    return ring

def print_grid(ring, n, m):
    max_digits = 1 if ring_num < 10 else 2
    for i in range(n):
        row = []
        for j in range(m):
            if ring[i][j] == 0:
                row.append('.' * max_digits)
            else:
                ring_str = str(ring[i][j])
                row.append(' ' * (max_digits - len(ring_str)) + ring_str)
        print(''.join(row))

n, m = map(int, input().split())
grid = [input() for _ in range(n)]
ring = fill_rings(grid, n, m)
print_grid(ring, n, m)