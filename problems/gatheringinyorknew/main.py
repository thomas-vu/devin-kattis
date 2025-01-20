def min_time_to_portals(h, hunters):
    # Sort the locations of the hunters
    hunters.sort()
    
    # Initialize left and right pointers for portals positions
    left = 0
    right = hunters[-1] - hunters[0]
    
    # Binary search for the optimal position of portals
    while left < right:
        mid = (left + right) // 2
        
        # Check the total time if portals are placed at mid and mid + hunters[0]
        left_time = max(hunters[i] - (mid + hunters[0]) for i in range(h))
        right_time = max(hunters[-i - 1] - (right - mid) for i in range(h))
        
        # Update the pointers based on the comparison of left_time and right_time
        if left_time < right_time:
            right = mid
        else:
            left = mid + 1
    
    # Calculate the total time with the optimal portals positions
    min_time = 0
    for hunter in hunters:
        min_time = max(min_time, abs(hunter - left))
    
    return min_time

# Read input
h = int(input())
hunters = list(map(int, input().split()))

# Output the result
print(min_time_to_portals(h, hunters))