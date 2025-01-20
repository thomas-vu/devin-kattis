def min_cost(s, p, m, n, trips):
    # Sort the trip days in non-decreasing order
    trips.sort()
    
    # Initialize variables to keep track of the minimum cost
    min_cost = 0
    
    # Iterate through each trip day to determine the best ticket purchase strategy
    for i in range(n):
        # Calculate the cost of buying individual tickets until this trip day
        min_cost += s * (trips[i] // m + 1)
    
    # Compare the total cost of individual tickets with the price of a period ticket
    min_cost = min(min_cost, p)
    
    return min_cost

# Read input from stdin
s, p, m, n = map(int, input().split())
trips = list(map(int, input().split()))

# Calculate and print the minimum cost of making the trips
print(min_cost(s, p, m, n, trips))