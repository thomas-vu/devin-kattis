def is_valid_tiling(grid, n):
    def count_unique_triominos(grid):
        triominos = set()
        for row in grid:
            for num in row:
                if num != 0:
                    triominos.add(num)
        return len(triominos)

    def cover_with_triominoes(grid, x1, y1, x2, y2, color):
        if (x2 - x1 + 1) % 2 != 0 or (y2 - y1 + 1) % 2 != 0:
            return False
        if x2 - x1 == 0 and y2 - y1 == 0:
            grid[x1][y1] = color
            return True
        size = (x2 - x1 + 1) // 2
        if cover_with_triominoes(grid, x1, y1, x1 + size - 1, y1 + size - 1, color) and \
           cover_with_triominoes(grid, x1 + size, y1, x2, y1 + size - 1, color) and \
           cover_with_triominoes(grid, x1, y1 + size, x1 + size - 1, y2, color) and \
           cover_with_triominoes(grid, x1 + size, y1 + size, x2, y2, color):
            return True
        return False

    def check_tiling(grid, n):
        unique_colors = count_unique_triominos(grid)
        if unique_colors != (4**n - 1) // 3:
            return False
        color_count = [[0] * (2**n) for _ in range(2**n)]
        for i in range(2**n):
            for j in range(2**n):
                if grid[i][j] != 0:
                    color_count[i][j] = 1
        if sum(sum(row) for row in color_count) != (4**n - 1) // 3:
            return False
        if sum(sum(row) for row in color_count) + 1 != (2**n) * (2**n):
            return False
        return True

    def place_triominoes(grid, n):
        if n == 1:
            for i in range(2**n):
                for j in range(2**n):
                    if grid[i][j] == 0:
                        x1, y1 = i, j
                    else:
                        x2, y2 = i, j
            grid[x1][y1] = 999
            return True
        size = 2**(n-1)
        for i in range(0, 2**n, size):
            for j in range(0, 2**n, size):
                if grid[i][j] == 0:
                    x1, y1 = i, j
                else:
                    x2, y2 = i, j
        if place_triominoes(grid, n-1):
            return True
        grid[x1][y1] = 999
        grid[x2][y2] = 999
        return True

    if check_tiling(grid, n):
        return 1
    else:
        return 0

# Example usage:
n = int(input())
grid = [list(map(int, input().split())) for _ in range(2**n)]
print(is_valid_tiling(grid, n))