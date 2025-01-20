def max_profit(prices):
    n = len(prices)
    if n == 0:
        return 0
    
    # Initialize variables to store the maximum profit and minimum price found so far
    max_profit = 0
    min_price = prices[0]
    
    # Traverse through the list of prices to find the maximum profit
    for i in range(1, n):
        # Update the minimum price found so far
        min_price = min(min_price, prices[i])
        # Update the maximum profit if selling on the current day gives a better profit
        max_profit = max(max_profit, prices[i] - min_price)
    
    return max_profit

# Read the number of predictions
N = int(input())
# Read the list of predicted prices
prices = list(map(int, input().split()))
# Output the maximum profit
print(max_profit(prices))