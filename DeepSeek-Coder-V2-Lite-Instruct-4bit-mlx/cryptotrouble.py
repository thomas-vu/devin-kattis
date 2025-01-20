MOD = 10**9 + 7

def is_valid(subset):
    num = int(subset)
    return num % 3 == 0

def count_valid_subsets(s):
    n = len(s)
    dp = [0] * (n + 1)
    dp[0] = 1
    
    for i in range(n):
        dp[i + 1] = dp[i]
        if s[i] == '0':
            continue
        for j in range(i, -1, -1):
            if is_valid(''.join(s[j:i + 1])):
                dp[i + 1] = (dp[i + 1] + dp[j]) % MOD
    
    return dp[n]

# Read input
N = int(input())
S = input()

# Compute and output the result
result = count_valid_subsets(S)
print(result)