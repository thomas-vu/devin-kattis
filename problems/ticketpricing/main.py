def solve(N, W, estimates):
    dp = [[0 for _ in range(N + 1)] for _ in range(W + 1)]
    ticket_price = [[0 for _ in range(N + 1)] for _ in range(W + 1)]
    
    for week in range(W - 1, -1, -1):
        for seats_left in range(N + 1):
            max_rev = 0
            best_price = 0
            for i in range(len(estimates[week][1])):
                price = estimates[week][1][i]
                tickets_sold = min(seats_left, estimates[week][2][i])
                rev = price * tickets_sold + dp[week + 1][seats_left - tickets_sold]
                if rev > max_rev:
                    max_rev = rev
                    best_price = price
            dp[week][seats_left] = max_rev
            ticket_price[week][seats_left] = best_price
    
    return dp[0][N], ticket_price[0][N]

# Read input
import sys
input = sys.stdin.read
data = input().split()
index = 0
N, W = int(data[index]), int(data[index + 1])
index += 2
estimates = []
for _ in range(W):
    K = int(data[index])
    prices = list(map(int, data[index + 1: index + K + 1]))
    tickets = list(map(int, data[index + K + 1: index + 2 * K + 1]))
    estimates.append((prices, tickets))
    index += 2 * K + 1

# Solve the problem and print output
max_rev, price = solve(N, W, estimates)
print(max_rev)
print(price)