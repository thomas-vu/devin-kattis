MOD = 10**9 + 7

def count_trees(h, w):
    # Initialize a DP table with dimensions (h+1) x (w+1)
    dp = [[[0] * (w + 1) for _ in range(h + 1)] for __ in range(2)]
    
    # Base case: a tree with height 0 and weight 0 has exactly one tree (the empty tree)
    dp[0][0][0] = 1
    
    # Build the DP table
    for height in range(h + 1):
        for weight in range(w + 1):
            if height > 0:
                # Vertical branch adds to both height and weight
                for branches in range(1, w + 1):
                    if height + branches <= h and weight * branches <= w:
                        dp[1][height + branches][weight * branches] += dp[0][height][weight]
                        dp[1][height + branches][weight * branches] %= MOD
            
            # Copy the current state to the next iteration
            for k in range(w + 1):
                dp[0][height][k] = (dp[0][height][k] + dp[1][height][k]) % MOD
                dp[1][height][k] = 0
    
    # The final answer is the number of ways to form a tree with height h and weight w
    return dp[0][h][w]

# Read input
import sys
input = sys.stdin.read
h, w = map(int, input().split())

# Output the result
print(count_trees(h, w))