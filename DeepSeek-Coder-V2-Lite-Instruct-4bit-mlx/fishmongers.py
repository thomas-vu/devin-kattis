def max_profit(n, m, weights, fishmongers):
    # Sort the fish by weight in ascending order
    weights.sort()
    
    # Helper function to calculate the total profit for a given fishmonger
    def get_profit(fishmonger):
        price, quantity = fishmonger
        total_weight = sum(weights[:quantity])
        return total_weight * price
    
    # Sort the fishmongers by price per kilogram in ascending order
    fishmongers.sort(key=lambda x: x[1])
    
    max_profit = 0
    j = 0
    
    # Sell fish to the first m fishmongers that offer the best price per kilogram
    for i in range(m):
        while j < n and weights[j] <= fishmongers[i][0]:
            max_profit += weights[j] * fishmongers[i][1]
            j += 1
    
    return max_profit

# Read input
n, m = map(int, input().split())
weights = list(map(int, input().split()))
fishmongers = [list(map(int, input().split())) for _ in range(m)]

# Calculate and print the maximum profit
print(max_profit(n, m, weights, fishmongers))