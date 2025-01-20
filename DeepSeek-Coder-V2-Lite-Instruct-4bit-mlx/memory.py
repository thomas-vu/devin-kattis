MOD = 1000000009

def count_representations(binary_str):
    n = len(binary_str)
    dp = [0] * (n + 1)
    dp[0] = 1
    
    for i in range(n):
        if binary_str[i] == '1':
            dp[i + 1] = (dp[i + 1] + dp[i]) % MOD
        if i > 0 and binary_str[i - 1] == '1' and binary_str[i] == '1':
            dp[i + 1] = (dp[i + 1] + dp[i - 1]) % MOD
    
    return dp[-1]

# Read input
binary_str = input().strip()

# Output the result
print(count_representations(binary_str))