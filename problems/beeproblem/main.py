def count_empty(grid, n, m):
    empty_count = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '.':
                empty_count += 1
    return empty_count

def fill_honey(grid, n, m):
    honey = [[0] * m for _ in range(n)]
    directions = [(-1, -1), (-1, 0), (0, -1), (0, 1), (1, 0), (1, 1)]
    
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '#':
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] == '.':
                        honey[ni][nj] = 1
    
    return sum(sum(row) for row in honey)

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    h, n, m = int(data[idx]), int(data[idx + 1]), int(data[idx + 2])
    idx += 3
    
    grid = []
    for i in range(n):
        row = []
        for j in range(m):
            if data[idx] == '.':
                row.append('.')
            else:
                row.append('#')
            idx += 1
        grid.append(row)
    
    empty_count = count_empty(grid, n, m)
    honey_needed = min(h, empty_count)
    
    print(fill_honey(grid, n, m))

if __name__ == "__main__":
    main()