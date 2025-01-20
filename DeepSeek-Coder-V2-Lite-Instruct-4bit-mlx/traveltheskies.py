def is_optimal(k, n, m, flights):
    from collections import defaultdict

    # Create a graph to represent the flights and capacities
    flight_graph = defaultdict(lambda: defaultdict(int))
    
    # Populate the flight graph with capacities and demands
    for u, v, d, z in flights:
        flight_graph[u][v] = z  # Capacity from u to v on day d
    
    # Create a list of demands for each airport-day pair
    demands = defaultdict(int)
    for a, b, c in customers:
        demands[(a, b)] += c
    
    # Check if all flights can be filled to capacity using DFS
    def dfs(airport, day):
        if day > n:
            return True  # All flights filled successfully
        
        for dest, cap in flight_graph[airport].items():
            if demands[(dest, day)] > 0 and cap > 0:
                demands[(dest, day)] -= 1
                if dfs(dest, day + 1):
                    return True
                demands[(dest, day)] += 1
        return False
    
    # Try to fill all flights starting from any airport on day 1
    for i in range(1, k + 1):
        if demands[(i, 1)] > 0 and dfs(i, 2):
            return "optimal"
    
    return "suboptimal"

# Read input
k, n, m = map(int, input().split())
flights = []
for _ in range(m):
    u, v, d, z = map(int, input().split())
    flights.append((u, v, d, z))
customers = []
for _ in range(int(k * n)):
    a, b, c = map(int, input().split())
    customers.append((a, b, c))

# Output the result
print(is_optimal(k, n, m, flights))