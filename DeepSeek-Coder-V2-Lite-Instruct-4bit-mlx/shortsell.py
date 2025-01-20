def maximum_profit(N, K, prices):
    max_profit = 0
    min_price = float('inf')
    
    for i in range(N):
        if prices[i] < min_price:
            min_price = prices[i]
        profit = (min_price - prices[i]) * 100 - K * (i + 1)
        if profit > max_profit:
            max_profit = profit
    
    return max(max_profit, 0)

# Read input
N, K = map(int, input().split())
prices = list(map(int, input().split()))

# Calculate and output the maximum profit
print("{:.1f}".format(maximum_profit(N, K, prices)))