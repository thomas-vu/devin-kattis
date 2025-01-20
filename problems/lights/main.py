# This problem is a bit complex, and involves combinatorics and dynamic programming to solve it efficiently.
# The key idea is to use the properties of binary states and the fact that each switch press can be thought of as flipping a bit in a binary string.
# We will use dynamic programming to count the number of ways to achieve the desired state after a certain number of moves.

MOD = 10567201

def count_ways(n, m, v):
    # Base case: if the number of moves is 0 and the desired state has v bulbs on, there's exactly one way (doing nothing)
    if v == 0:
        return pow(2, n - m, MOD)
    
    # Initialize a DP table where dp[i][j] represents the number of ways to have j bulbs on after i moves
    dp = [[0] * (v + 1) for _ in range(m + 1)]
    dp[0][v] = 1  # Base case: after 0 moves, we want v bulbs on
    
    for i in range(1, m + 1):
        for j in range(v + 1):
            # Recurrence relation: dp[i][j] = sum(dp[i-1][k]) for all k such that (k + j) is even
            # This means the number of ways to get to state j with i moves is the sum of ways to get to states that, when combined with j, result in an even number of bulbs on
            for k in range(n + 1):
                if (k + j) % 2 == 0:
                    dp[i][j] = (dp[i][j] + dp[i-1][k]) % MOD
    
    # The final answer is the number of ways to have exactly v bulbs on after m moves
    return dp[m][0]

# Process the input and output the results
while True:
    n, m, v = map(int, input().split())
    if n == 0 and m == 0 and v == 0:
        break
    result = count_ways(n, m, v)
    print(result)