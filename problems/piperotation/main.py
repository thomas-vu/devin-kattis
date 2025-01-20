def is_possible(grid, N, M):
    # Check the outer edges for pipes
    for j in range(M):
        if grid[0][j] != 'A':
            return "Impossible"
    for j in range(M):
        if grid[N - 1][j] != 'A':
            return "Impossible"
    for i in range(N):
        if grid[i][0] != 'A':
            return "Impossible"
    for i in range(N):
        if grid[i][M - 1] != 'A':
            return "Impossible"
    
    # Check the inner edges for pipes
    for i in range(1, N - 1):
        for j in range(1, M - 1):
            if grid[i][j] == 'B':
                if (grid[i - 1][j] != 'C' and grid[i - 1][j] != 'D') or (grid[i + 1][j] != 'C' and grid[i + 1][j] != 'D'):
                    return "Impossible"
                if (grid[i][j - 1] != 'C' and grid[i][j - 1] != 'D') or (grid[i][j + 1] != 'C' and grid[i][j + 1] != 'D'):
                    return "Impossible"
            elif grid[i][j] == 'C':
                if (grid[i - 1][j] != 'B' and grid[i - 1][j] != 'D') or (grid[i + 1][j] != 'B' and grid[i + 1][j] != 'D'):
                    return "Impossible"
                if (grid[i][j - 1] != 'B' and grid[i][j - 1] != 'D') or (grid[i][j + 1] != 'B' and grid[i][j + 1] != 'D'):
                    return "Impossible"
            elif grid[i][j] == 'D':
                if (grid[i - 1][j] != 'B' and grid[i - 1][j] != 'C') or (grid[i + 1][j] != 'B' and grid[i + 1][j] != 'C'):
                    return "Impossible"
                if (grid[i][j - 1] != 'B' and grid[i][j - 1] != 'C') or (grid[i][j + 1] != 'B' and grid[i][j + 1] != 'C'):
                    return "Impossible"
    
    return "Possible"

# Read input
N, M = map(int, input().split())
grid = [input() for _ in range(N)]

# Check if possible and print the result
print(is_possible(grid, N, M))