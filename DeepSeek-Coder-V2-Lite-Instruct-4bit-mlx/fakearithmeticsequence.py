def longest_subsequence(n, a):
    dp = [1] * n
    for i in range(n):
        for j in range(i):
            if abs(a[i] - a[j]) == (a[j] + a[i]):
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp) if n > 0 else 0

n = int(input())
a = list(map(int, input().split()))
print(longest_subsequence(n, a))