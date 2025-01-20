def solve(n, r, c, passengers):
    # Create a 2D grid to store the number of passengers that can be placed at each seat
    # dp[i][j] will store the maximum number of passengers that can be placed at row i, column j
    dp = [[0] * (c + 1) for _ in range(r + 1)]
    
    # Process each passenger's preference
    for a_i, b_i, s_i in passengers:
        # Update the dp grid based on the passenger's preference
        for i in range(1, r + 1):
            for j in range(1, c + 1):
                if abs(a_i - i) <= s_i and abs(b_i - j) <= s_i:
                    dp[i][j] = max(dp[i][j], dp[a_i - (s_i if a_i > i else 0)][b_i - (s_i if b_i > j else 0)] + 1)
    
    # The result is the maximum value in the dp grid
    return max(max(row) for row in dp)

# Read input
n, r, c = map(int, input().split())
passengers = [tuple(map(int, input().split())) for _ in range(n)]

# Solve the problem and output the result
print(solve(n, r, c, passengers))