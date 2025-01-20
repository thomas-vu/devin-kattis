def count_tilings(n):
    if n == 0:
        return 1
    elif n < 3:
        return 0
    
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[2] = 3
    
    for i in range(4, n + 1, 2):
        dp[i] = 4 * dp[i - 2] - dp[i - 4]
    
    return dp[n]

tilings = []
while True:
    n = int(input())
    if n == -1:
        break
    tilings.append(count_tilings(n))

for tiling in tilings:
    print(tiling)