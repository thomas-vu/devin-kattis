def time_until_empty(t, s, n, flips):
    # Calculate the total amount of sand that needs to flow through the hourglass
    total_sand = s
    
    # Sort and remove duplicates from flips list
    flips.sort()
    unique_flips = [flips[0]]
    for i in range(1, n):
        if flips[i] != unique_flips[-1]:
            unique_flips.append(flips[i])
    
    # Calculate the amount of sand that has flowed through the hourglass so far
    for flip_time in unique_flips:
        if flip_time < t:
            continue
        total_sand += (flip_time - t)
    
    # Calculate the time needed for all sand to flow through the hourglass
    if total_sand <= 0:
        return 0
    else:
        time_needed = total_sand
        return time_needed

# Read input from stdin
import sys
input = sys.stdin.read
data = input().split()
t, s, n = int(data[0]), int(data[1]), int(data[2])
flips = list(map(int, data[3:]))

# Get the result and print it
result = time_until_empty(t, s, n, flips)
print(result)