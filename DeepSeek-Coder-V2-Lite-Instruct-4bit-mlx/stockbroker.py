def max_profit(prices):
    n = len(prices)
    if n == 0:
        return 0
    
    # Create two lists to store the maximum profit if we hold a share or not on each day
    hold = [0] * n
    sell = [0] * n
    
    # Base cases
    hold[0] = -prices[0]  # Buying the first share on day 0
    sell[0] = 0  # Not holding any shares initially
    
    for i in range(1, n):
        # If we hold a share on day i, we could have bought it on any previous day or did nothing
        hold[i] = max(hold[i-1], sell[i-1] - prices[i])
        # If we sell a share on day i, we could have sold it on any previous day or did nothing
        sell[i] = max(sell[i-1], hold[i-1] + prices[i])
    
    # The maximum profit on the last day is either by selling all shares or holding them till the end
    return sell[-1]

# Read input
d = int(input())
prices = [int(input()) for _ in range(d)]

# Calculate and print the result
print(max_profit(prices))