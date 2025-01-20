def find_optimal_path(r, c, n, elevations):
    # Initialize the minimum sum with a large number
    min_sum = float('inf')
    
    # Directions for moving in the grid: East, Northeast, Southeast
    directions = [(0, 1), (1, 1), (1, -1)]
    
    # Function to check if a cell is within the bounds of the grid
    def in_bounds(x, y):
        return 0 <= x < r and 0 <= y < c
    
    # Function to find the minimum path sum with exactly n passes
    def dfs(x, y, path_sum, passed):
        nonlocal min_sum
        
        # If we have reached the Eastern border and have exactly n passes
        if y == c:
            if passed == n:
                min_sum = min(min_sum, path_sum)
            return
        
        # If we have reached the Eastern border but passed is not n
        if y == c - 1:
            return
        
        # Explore all possible moves
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if in_bounds(nx, ny) and elevations[nx][ny] != -1:
                if dx == 0 and dy == 1:  # Moving East
                    dfs(nx, ny, path_sum + elevations[nx][ny], passed)
                elif dx == 1 and dy == 1:  # Moving Northeast
                    if elevations[nx][ny] > elevations[x][y]:
                        dfs(nx, ny, path_sum + elevations[nx][ny], passed + 1)
                elif dx == 1 and dy == -1:  # Moving Southeast
                    if elevations[nx][ny] > elevations[x][y]:
                        dfs(nx, ny, path_sum + elevations[nx][ny], passed + 1)
    
    # Start DFS from each Western border cell
    for i in range(r):
        if elevations[i][0] != -1:
            dfs(i, 0, elevations[i][0], 0)
    
    # Return the minimum sum found or 'impossible' if no path was found
    return min_sum if min_sum != float('inf') else 'impossible'

# Main function to read input and output the result
def main():
    r, c, n = map(int, input().split())
    elevations = [list(map(int, input().split())) for _ in range(r)]
    result = find_optimal_path(r, c, n, elevations)
    print(result)

# Call the main function
if __name__ == "__main__":
    main()