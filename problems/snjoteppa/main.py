def can_drive(grid):
    n = len(grid[0])
    dp = [[False] * 3 for _ in range(n)]
    
    # Initialize the DP table based on the initial grid state
    for j in range(n):
        if grid[0][j] == 'o':
            dp[j][0] = True
        if grid[1][j] == 'o':
            dp[j][1] = True
    
    # Process each query
    for _ in range(n):
        update = input().split()
        if update[0] == 'U':
            x, y = int(update[1]) - 1, int(update[2]) - 1
            if grid[x][y] == '.':
                grid[x][y] = 'o'
            else:
                grid[x][y] = '.'
        elif update[0] == 'Q':
            if dp[-1][0] or dp[-1][1]:
                print("Jebb")
            else:
                print("Neibb")