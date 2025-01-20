def min_possible_cost(N, flight_prices):
    max_price = max(flight_prices)
    half_max_price = max_price // 2
    
    min_cost = float('inf')
    for price in flight_prices:
        if half_max_price >= price:
            net_cost = 0
        else:
            net_cost = price - half_max_price
        min_cost = min(min_cost, net_cost)
    
    return int(min_cost)

# Read input
N = int(input())
flight_prices = [int(input()) for _ in range(N)]

# Calculate and output the minimum possible cost
print(min_possible_cost(N, flight_prices))