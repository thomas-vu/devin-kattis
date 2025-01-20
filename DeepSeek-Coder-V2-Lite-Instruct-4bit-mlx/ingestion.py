def max_calories(n, m, courses):
    dp = [0] * (n + 3)
    for i in range(n - 1, -1, -1):
        dp[i] = max(dp[i + 1], courses[i] + (0 if i + 2 > n - 1 else dp[i + 2]))
    return m + sum(dp[:n])

# Read input
import sys
input = sys.stdin.read
data = input().split()
n, m = int(data[0]), int(data[1])
courses = list(map(int, data[2:]))

# Calculate and print the result
print(max_calories(n, m, courses))