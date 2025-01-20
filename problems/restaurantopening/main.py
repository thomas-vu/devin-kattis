def min_total_cost(n, m, grid):
    # Helper function to calculate the minimum distance from a given position to all points in the grid
    def min_distance(r, c):
        dist = float('inf')
        for i in range(n):
            for j in range(m):
                dist = min(dist, abs(r - i) + abs(c - j))
        return dist
    
    total_cost = float('inf')
    for i in range(n):
        for j in range(m):
            current_cost = 0
            for x in range(n):
                for y in range(m):
                    current_cost += grid[x][y] * min_distance(x, y)
            total_cost = min(total_cost, current_cost)
    return total_cost

# Read input
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Output the result
print(min_total_cost(n, m, grid))