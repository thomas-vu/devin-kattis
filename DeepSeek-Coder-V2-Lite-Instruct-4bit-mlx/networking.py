def max_credits(N, K, courses):
    dp = [0] * (K + 1)
    for i in range(N):
        credits, lecturer = courses[i]
        for j in range(K - credits + 1)[::-1]:
            if dp[j] > 0 or j == 0:
                dp[j + credits] = max(dp[j + credits], dp[j] + (1 if j == 0 else 0))
    for i in range(K, -1, -1):
        if dp[i] > 0:
            return i

N, K = map(int, input().split())
courses = []
for _ in range(N):
    credits, lecturer = input().split()
    courses.append((int(credits), lecturer))
print(max_credits(N, K, courses))