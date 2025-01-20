def min_days_to_retire(n, M, investments):
    # Sort investments by the profit-to-cost ratio in descending order
    investments.sort(key=lambda x: (-x[0] / x[1], x[1]))
    
    days = 0
    current_wealth = 0
    
    for profit, cost in investments:
        while current_wealth < cost:
            # Invest in the best available option until we can pay back the friend
            current_wealth += profit
            days += 1
        # After paying back the friend, we have the remaining money left to retire
        current_wealth -= cost
    
    # Check if we have enough money to retire comfortably
    while current_wealth < M:
        # Keep investing until we reach the minimum required wealth
        for profit, cost in investments:
            current_wealth += profit
            days += 1
        if days > 10**5:  # Prune the search to avoid infinite loops
            break
    
    return days

# Read input
n, M = map(int, input().split())
investments = [tuple(map(int, input().split())) for _ in range(n)]

# Calculate and print the result
print(min_days_to_retire(n, M, investments))