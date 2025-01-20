def min_cost_to_power_island(n, m, cities, costs):
    # Initialize the minimum cost to a large number
    min_cost = float('inf')
    
    # Iterate through all possible locations for the power plant
    for i in range(m):
        # Calculate the cost if a power plant is built at city c_i with cost a_i
        build_cost = cities[i][1]
        # Calculate the total cost of powering all cities with this configuration
        current_cost = build_cost
        
        # Calculate the cost of building power lines between adjacent cities
        for j in range(1, n):
            if j == n - 1:
                current_cost += min(costs[j], costs[(cities[i][0] - j) % n])
            else:
                current_cost += min(costs[j], costs[(cities[i][0] - j) % n])
        
        # Update the minimum cost if the current configuration is cheaper
        min_cost = min(min_cost, current_cost)
    
    return min_cost

# Read input from stdin
n, m = map(int, input().split())
cities = [tuple(map(int, input().split())) for _ in range(m)]
costs = list(map(int, input().split()))

# Output the minimum cost of powering all cities on the island
print(min_cost_to_power_island(n, m, cities, costs))