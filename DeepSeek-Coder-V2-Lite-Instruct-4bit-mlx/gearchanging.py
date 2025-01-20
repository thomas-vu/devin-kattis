def can_ride(N, M, P, crank_teeth, wheel_teeth):
    # Calculate the current and new cadence for each gear change
    min_ratio = float('inf')
    max_ratio = 0.0
    
    for i in range(N):
        for j in range(M):
            ratio = crank_teeth[i] / wheel_teeth[j]
            min_ratio = min(min_ratio, ratio)
            max_ratio = max(max_ratio, ratio)
    
    # Check if the maximum allowed change is respected
    max_change = (max_ratio - min_ratio) / min_ratio * 100
    
    return "Ride on!" if max_change <= P else "Time to change gears!"

# Read input
N, M, P = map(int, input().split())
crank_teeth = list(map(int, input().split()))
wheel_teeth = list(map(int, input().split()))

# Output the result
print(can_ride(N, M, P, crank_teeth, wheel_teeth))