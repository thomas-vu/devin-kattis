def calculate_minimum_distance(n, p, distances):
    # Sort the distances in ascending order
    sorted_distances = sorted(distances)
    
    # Initialize the minimum distance to keep
    min_distance = float('inf')
    
    # Iterate through the sorted distances to find the minimum distance needed
    for i in range(n):
        # Calculate the required distance to keep to the car directly in front
        current_distance = sorted_distances[i] - (p * i)
        # Update the minimum distance if a smaller one is found
        min_distance = min(min_distance, current_distance)
    
    return min_distance

# Read input
n, p = map(int, input().split())
distances = list(map(int, input().split()))

# Calculate and output the result
result = calculate_minimum_distance(n, p, distances)
print(result)