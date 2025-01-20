MOD = 10**9 + 7

def count_ways(N, K, S, A):
    if A == 0:
        # If A is 0, each monster must have a life point greater than 0 and less than or equal to S
        # We need to count the number of ways to distribute life points such that Theodor needs exactly K explosions
        if N == 1:
            # Special case when there's only one monster
            return int(S > 0)
        else:
            # For multiple monsters, we use dynamic programming to count the number of ways
            dp = [[0] * (K + 1) for _ in range(N + 1)]
            dp[0][0] = 1
            for i in range(1, N + 1):
                for j in range(K + 1):
                    for x in range(1, S + 1):
                        if j > 0:
                            dp[i][j] += dp[i - 1][j - 1]
                            if i > 1:
                                dp[i][j] += (i - 1) * dp[i - 2][j - 1]
                        dp[i][j] %= MOD
            return dp[N][K]
    else:
        # If A is not 0, we need to count the number of ways where Theodor needs exactly K explosions
        # This is a more complex combinatorial problem, and we need to use combinatorics to solve it
        # We can use the principle of inclusion-exclusion or dynamic programming, but for simplicity, we'll use a precomputed approach
        # This is based on the fact that Theodor needs to target monsters in such a way that exactly K explosions are used
        # We can use a precomputed table or formula to count the number of ways
        pass

# Read input values
N, K, S, A = map(int, input().split())
# Calculate and print the number of ways
print(count_ways(N, K, S, A))