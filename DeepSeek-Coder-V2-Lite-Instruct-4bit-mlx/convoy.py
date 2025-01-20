def min_time_to_transport_people(n, k, times):
    # Sort the driving times to optimize the process
    times.sort()
    
    # Initialize variables for the minimum and maximum possible time to transport all people
    min_time = 0
    max_time = 0
    
    # Use two pointers to simulate the process of transporting people with cars
    left = 0
    right = n - 1
    
    while left <= right:
        # Calculate the time for the current trip with a car carrying up to 5 people
        current_time = times[right] + times[left]
        
        # Update the minimum and maximum possible time
        min_time = max(min_time, current_time)
        
        # Move the pointers to simulate the next trip
        left += 1
        right -= 1
    
    return min_time

# Read input from standard in
import sys
input = sys.stdin.read
data = input().split()

n = int(data[0])
k = int(data[1])
times = list(map(int, data[2:]))

# Calculate and print the result
result = min_time_to_transport_people(n, k, times)
print(result)