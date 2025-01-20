MOD = 10**9 + 7

def count_partitions(n, m, digits):
    dp = [0] * (n + 1)
    suff_sum = [0] * (n + 1)
    dp[0] = 1
    
    for i in range(n):
        num = 0
        for j in range(i, n):
            num = (num * 10 + int(digits[j])) % m
            if num == 0:
                dp[j + 1] = (dp[j + 1] + dp[i]) % MOD
    
    return dp[n]

# Read input
n, m = map(int, input().split())
digits = input()

# Calculate and output the result
result = count_partitions(n, m, digits)
print(result)