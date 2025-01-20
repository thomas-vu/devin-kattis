import sys
from math import inf

def latest_possible_departure(n, m, s, tram_lines):
    # Initialize the latest time to leave as -inf for unreachable case
    latest_leave = -inf
    
    # Create a list to store the earliest arrival times for each stop
    earliest_arrival = [inf] * n
    
    # The latest time to leave the hotel is when we arrive at stop n-1 on time
    earliest_arrival[0] = 0
    
    # Process each tram line to update the earliest arrival times
    for u, v, t0, p, d in tram_lines:
        # Process each tram of this line
        for t in range(t0, s + 1, p):
            # Check if the tram can reach the destination by the meeting time
            arrival_time = t + d
            if arrival_time <= s:
                # Update the earliest arrival time for each stop this tram passes through
                for i in range(n):
                    if (i - u) % (v - u) == 0:
                        earliest_arrival[i] = min(earliest_arrival[i], arrival_time)
    
    # The latest time to leave the hotel is when we arrive at stop n-1 on time
    if earliest_arrival[n - 1] != inf:
        latest_leave = s - earliest_arrival[n - 1]
    
    return latest_leave if latest_leave != -inf else "impossible"

# Read input from stdin
n, m, s = map(int, sys.stdin.readline().split())
tram_lines = [tuple(map(int, sys.stdin.readline().split())) for _ in range(m)]

# Get the latest possible departure time
result = latest_possible_departure(n, m, s, tram_lines)

# Print the result
print(result)