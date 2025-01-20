def min_bottles(s, v1, v2):
    # Check if it's possible to fill the bottles with the given volumes
    if s < v2:
        return "Impossible"
    
    # Calculate the maximum number of bottles of each type that can be used
    max_v1 = s // v1
    remaining = s % v1
    
    # Check if the remaining volume can be filled by the smaller bottle
    max_v2 = 0 if remaining != 0 else (s // v2)
    
    # Check if the total volume can be exactly filled by either type of bottle
    for i in range(max_v1 + 1):
        if (s - i * v1) % v2 == 0:
            max_v2 = (s - i * v1) // v2
            break
    
    return f"{max_v1} {max_v2}" if max_v2 != 0 else "Impossible"

# Read input
s, v1, v2 = map(int, input().split())

# Output the result
print(min_bottles(s, v1, v2))