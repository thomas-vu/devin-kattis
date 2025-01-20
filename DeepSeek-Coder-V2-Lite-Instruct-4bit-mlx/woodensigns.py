MOD = 2**31 - 1

def count_signs(N, positions):
    # Create a list to store the number of ways to fix each arrowhead
    dp = [0] * (N + 1)
    # Initialize the number of ways to fix the bottom arrowhead
    dp[0] = 1
    
    for i in range(N):
        # Update the number of ways to fix each arrowhead based on the current position
        for j in range(i, -1, -1):
            if positions[j] < positions[i]:
                dp[i + 1] = (dp[i + 1] + dp[j]) % MOD
            else:
                break
    
    # The total number of distinct signs is the sum of ways to fix all arrowheads
    return dp[N]

# Read input
N = int(input().strip())
positions = list(map(int, input().split()))

# Compute and print the result
print(count_signs(N, positions))