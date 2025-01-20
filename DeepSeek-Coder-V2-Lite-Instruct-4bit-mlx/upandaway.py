def min_time_to_vacation(n, x, k, heights, travel_times):
    # Initialize the minimum time to a large number
    min_time = float('inf')
    
    # Use bitmask to generate all possible states of using fireworks
    for mask in range(1 << k):
        time_taken = 0
        total_elevation_gain = 0
        
        # Simulate the journey using fireworks if needed
        for i in range(n):
            if (mask >> i) & 1:
                for j in range(n):
                    if heights[i] > heights[j]:
                        total_elevation_gain += heights[i] - heights[j]
                    elif (mask >> j) & 1 and heights[i] < heights[j]:
                        total_elevation_gain += heights[j] - heights[i]
        
        # Check if the journey is valid and update the minimum time
        if total_elevation_gain <= k:
            for i in range(n):
                for j in range(n):
                    if (heights[i] > heights[j] and i == x - 1) or (heights[i] < heights[j] and j == x - 1):
                        time_taken += travel_times[i][j]
            min_time = min(min_time, time_taken)
    
    # Return the minimum time if possible, otherwise return -1
    return min_time if min_time != float('inf') else -1

# Read input
n, x, k = map(int, input().split())
heights = list(map(int, input().split()))
travel_times = [list(map(int, input().split())) for _ in range(n)]

# Output the result
print(min_time_to_vacation(n, x, k, heights, travel_times))