def max_hot_yoga_time(N, durations):
    dp = [0] * N
    dp[0] = durations[0]
    
    for i in range(1, N):
        if durations[i] >= durations[i - 1]:
            dp[i] = dp[i - 1] + durations[i]
        else:
            dp[i] = dp[i - 1]
    
    return max(dp)

# Read input
N = int(input())
durations = list(map(int, input().split()))

# Calculate and output the result
print(max_hot_yoga_time(N, durations))