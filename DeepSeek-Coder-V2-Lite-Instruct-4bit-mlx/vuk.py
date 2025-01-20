def read_ints():
    return list(map(int, input().split()))

def read_grid(n, m):
    grid = []
    for _ in range(n):
        row = input().strip()
        grid.append(row)
    return grid

def find_positions(grid):
    V, J = None, None
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'V':
                V = (i, j)
            elif grid[i][j] == 'J':
                J = (i, j)
    return V, J

def distance(r1, c1, r2, c2):
    return abs(r1 - r2) + abs(c1 - c2)

def max_min_distance(grid, V, J):
    min_max_dist = float('inf')
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '+':
                dist = distance(V[0], V[1], i, j) + distance(i, j, J[0], J[1])
                min_max_dist = min(min_max_dist, dist)
    return min_max_dist

def main():
    N, M = read_ints()
    grid = read_grid(N, M)
    V, J = find_positions(grid)
    result = max_min_distance(grid, V, J)
    print(result)

if __name__ == "__main__":
    main()