def count_gold(grid):
    width, height = len(grid[0]), len(grid)
    player_pos = None
    
    # Find the player's starting position
    for y in range(height):
        for x in range(width):
            if grid[y][x] == 'P':
                player_pos = (x, y)
                break
        if player_pos:
            break
    
    # Helper function to check if a position is within bounds and not a wall
    def is_valid(x, y):
        return 0 <= x < width and 0 <= y < height and grid[y][x] != '#'
    
    # Directions for moving up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # Use DFS to explore the grid and count gold
    def dfs(x, y):
        if not is_valid(x, y) or grid[y][x] == 'T':
            return 0
        if grid[y][x] == 'G':
            gold = 1
        else:
            gold = 0
        
        # Mark the position as visited by setting it to a wall temporarily
        temp = grid[y][x]
        grid[y][x] = '#'
        
        # Explore all possible directions
        for dx, dy in directions:
            gold += dfs(x + dx, y + dy)
        
        # Restore the original position
        grid[y][x] = temp
        return gold
    
    # Start DFS from the player's position
    max_gold = dfs(player_pos[0], player_pos[1])
    return max_gold

# Read input
W, H = map(int, input().split())
grid = [list(input().strip()) for _ in range(H)]

# Output the result
print(count_gold(grid))