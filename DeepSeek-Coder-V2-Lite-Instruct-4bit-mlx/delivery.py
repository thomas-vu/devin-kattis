def min_distance(N, K, locations):
    total_distance = 0
    current_load = 0
    position = 0
    
    while locations:
        # Load letters at the current position
        load = 0
        while locations and load + locations[0][1] <= K:
            load += locations[0][1]
            current_position = locations.pop(0)
        
        # Travel to the next delivery location
        distance = abs(current_position[0] - position)
        total_distance += 2 * distance
        position = current_position[0]
        
    return total_distance

# Read input
N, K = map(int, input().split())
locations = [tuple(map(int, input().split())) for _ in range(N)]
locations.sort()  # Sort locations by their coordinates

# Calculate and output the minimum total travel distance
print(min_distance(N, K, locations))