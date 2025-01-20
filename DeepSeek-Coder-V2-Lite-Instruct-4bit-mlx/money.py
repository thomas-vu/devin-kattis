def read_ints():
    return list(map(int, input().split()))

m, n = read_ints()
producers = []
consumers = []

for _ in range(m):
    pi, di = read_ints()
    producers.append((pi, di))

for _ in range(n):
    qj, ej = read_ints()
    consumers.append((qj, ej))

# Sort producers by price and start date, consumers by buying price and end date
producers.sort(key=lambda x: (x[0], x[1]))
consumers.sort(key=lambda x: (x[0], x[1]))

# Initialize DP arrays
dp = [0] * (n + 1)
prev = [-1] * (n + 1)

# DP to find the maximum profit
for i in range(m):
    for j in range(n - 1, -1, -1):
        if producers[i][1] <= consumers[j][1]:
            if dp[j + 1] < dp[j] + (consumers[j][0] - producers[i][0]):
                dp[j + 1] = dp[j] + (consumers[j][0] - producers[i][0])
                prev[j + 1] = i

# Reconstruct the solution
max_profit = dp[n]
if max_profit == 0:
    print(max_profit)
else:
    path = []
    k = n
    while k > 0 and prev[k] != -1:
        path.append(prev[k])
        k -= 1
    print(max_profit)