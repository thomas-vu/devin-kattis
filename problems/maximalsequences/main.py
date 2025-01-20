from collections import defaultdict
import sys
input = sys.stdin.read
n = int(input().split()[1])
a = list(map(int, input().split()))
q = int(input().split()[1])
for _ in range(q):
    i, m = map(int, input().split())
    b = list(map(int, input().split()))
    dp = [0] * (n + 1)
    for j in range(i - 1, n):
        if a[j] in b:
            dp[j - i + 2] = dp[j - i + 1] + 1
        else:
            dp[j - i + 2] = 0
    print(max(dp))