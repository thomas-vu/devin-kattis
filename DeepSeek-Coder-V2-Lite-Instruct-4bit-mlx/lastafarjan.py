def max_cars_that_fit(N, L, car_lengths):
    dp = [[0] * (L + 1) for _ in range(N + 1)]
    
    for i in range(1, N + 1):
        for j in range(L + 1):
            if car_lengths[i - 1] <= j:
                dp[i][j] = max(dp[i - 1][j], 1 + dp[i - 1][j - car_lengths[i - 1]])
            else:
                dp[i][j] = dp[i - 1][j]
    
    return dp[N][L]

# Read input
N = int(input())
L = int(input())
car_lengths = list(map(int, input().split()))

# Calculate and print the result
print(max_cars_that_fit(N, L, car_lengths))