MOD = 10**9 + 7

def count_permutations(N, L, G):
    # Create a list to store the count of valid permutations ending with each number from 1 to N
    dp = [0] * (N + 1)
    # The number of valid permutations for a single element sequence is always 1
    dp[0] = 1
    
    for g in G:
        # For each element in the GIS sequence, update the dp array
        for i in range(N, g - 1, -1):
            dp[i] = (dp[i] + dp[i - g]) % MOD
    
    # The final answer is the sum of all valid permutations ending with any number from g_L to N
    result = sum(dp[g:] for g in G) % MOD
    return result

# Read input
N, L = map(int, input().split())
G = list(map(int, input().split()))

# Output the result
print(count_permutations(N, L, G))