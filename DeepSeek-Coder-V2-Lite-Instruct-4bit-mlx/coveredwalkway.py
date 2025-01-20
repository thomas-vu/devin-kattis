def min_cost_to_cover_points(n, c, points):
    # Initialize the minimum cost to cover all points starting from the first point
    min_cost = float('inf')
    
    # Iterate through the points to find the minimum cost to cover each segment
    for i in range(n):
        current_cost = c
        for j in range(i, n):
            distance = points[j] - (points[i] if i != j else 0)
            current_cost += distance ** 2
        min_cost = min(min_cost, current_cost)
    
    return min_cost

# Read input
n, c = map(int, input().split())
points = [int(input()) for _ in range(n)]

# Calculate and print the minimum cost
print(min_cost_to_cover_points(n, c, points))