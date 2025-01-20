def count_paths(Y, X, x_init, map):
    mod = 1000003
    
    # Initialize the DP array with zeros
    dp = [[[0] * (X) for _ in range(Y)] for _ in range(2)]
    
    # Starting position
    dp[0][Y-1][x_init] = 1
    
    # Process the map from bottom to top, left to right
    for y in range(Y-1, -1, -1):
        for x in range(X):
            if map[y][x] == '~' or map[y][x] == '@':
                # Update the DP array for both states (current and next)
                if y < Y-1:
                    dp[1][y][x] = (dp[1][y][x] + dp[0][y+1][x]) % mod
                if y > 0:
                    dp[1][y][x] = (dp[1][y][x] + dp[0][y-1][x]) % mod
                if x < X-1 and map[y][x+1] not in ['>', '#']:
                    dp[1][y][x] = (dp[1][y][x] + dp[0][y][x+1]) % mod
                if x > 0 and map[y][x-1] not in ['<', '#']:
                    dp[1][y][x] = (dp[1][y][x] + dp[0][y][x-1]) % mod
                
                # Move to the next state
                dp[0][y][x] = dp[1][y][x]
                dp[1][y][x] = 0
    
    # Check if the castle is reachable
    result = dp[0][0][x_init]
    if result == 0:
        return "begin repairs"
    else:
        return result

# Read input
Y, X, x_init = map(int, input().split())
map = [input() for _ in range(Y)]

# Output the result
print(count_paths(Y, X, x_init, map))