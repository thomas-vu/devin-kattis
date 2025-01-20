def find_message(grid):
    N = len(grid)
    M = len(grid[0])
    
    # Create a DP table to store the maximum path sum
    dp = [[0] * M for _ in range(N)]
    
    # Initialize the starting point
    dp[0][0] = 1 if grid[0][0] != '.' else 0
    
    # Fill the DP table
    for i in range(N):
        for j in range(M):
            if grid[i][j] != '.':
                if i > 0:
                    dp[i][j] += dp[i - 1][j]
                if j > 0:
                    dp[i][j] += dp[i][j - 1]
    
    # Reconstruct the message from the DP table
    message = []
    x, y = N - 1, M - 1
    while x >= 0 and y >= 0:
        if x > 0 and dp[x][y] == dp[x - 1][y]:
            x -= 1
        elif y > 0 and dp[x][y] == dp[x][y - 1]:
            y -= 1
        else:
            message.append(grid[x][y])
            x -= 1
            y -= 1
    
    return ''.join(reversed(message))

# Read input
N, M = map(int, input().split())
grid = [input() for _ in range(N)]

# Output the secret message
print(find_message(grid))