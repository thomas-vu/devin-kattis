def find_treasure(grid, r, c):
    treasure_positions = []
    
    for i in range(1, r-1):
        for j in range(1, c-1):
            if grid[i][j] == '0' and \
               grid[i-1][j-1] == 'O' and grid[i-1][j] == 'O' and grid[i-1][j+1] == 'O' and \
               grid[i][j-1] == 'O' and grid[i][j+1] == 'O' and \
               grid[i+1][j-1] == 'O' and grid[i+1][j] == 'O' and grid[i+1][j+1] == 'O':
                treasure_positions.append((i+1, j+1))
    
    if not treasure_positions:
        print("Oh no!")
    elif len(treasure_positions) == 1:
        print(*treasure_positions[0])
    else:
        print(f"Oh no! {len(treasure_positions)} locations")

# Read input
r, c = map(int, input().split())
grid = [input() for _ in range(r)]

# Find and print the treasure position
find_treasure(grid, r, c)