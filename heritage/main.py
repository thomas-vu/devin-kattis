import sys
input = sys.stdin.readline
MOD = 10**9 + 7

N, W = input().strip().split()
N = int(N)

words = []
for _ in range(N):
    line = input().strip().split()
    w, m = line[0], int(line[1])
    words.append((w, m))

length = len(W)
dp = [0] * (length + 1)
dp[length] = 1

for i in range(length - 1, -1, -1):
    for w, m in words:
        wl = len(w)
        if i + wl <= length and W[i:i+wl] == w:
            dp[i] = (dp[i] + dp[i+wl] * m) % MOD

print(dp[0] % MOD)
