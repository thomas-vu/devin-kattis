MOD = 10**9 + 7

def max_days(N, activities):
    activities.sort()
    dp = [1] * N
    
    for i in range(N):
        for j in range(i):
            if activities[j] < activities[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp) % MOD

# Read input
N = int(input())
activities = list(map(int, input().split()))

# Output the result
print(max_days(N, activities))