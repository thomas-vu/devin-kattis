def is_valid_solution(grid):
    n = len(grid)
    
    # Helper function to check if placing light bulbs in the grid is valid
    def is_valid(x, y):
        # Check all four directions for light bulbs count matching the blocked cell's number
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        count = 0
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n:
                if grid[nx][ny] == '?':
                    count += 1
                elif grid[nx][ny] in '01234':
                    required = int(grid[nx][ny])
                    if count == required:
                        return True
        return False
    
    # Main loop to check each cell in the grid
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 'X':  # Blocked cell, continue to the next
                continue
            if grid[i][j] in '01234':  # Blocked cell with a number
                if not is_valid(i, j):
                    return 0
            elif grid[i][j] == '.':  # Open cell, check if it's already lit
                if not is_valid(i, j):
                    return 0
    return 1

# Read input and process the grid
n = int(input())
grid = [input() for _ in range(n)]
print(is_valid_solution(grid))