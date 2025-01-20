def calculate_bridge_unavailability(arrival_times):
    n = len(arrival_times)
    if n == 0:
        return 0
    
    # Sort the arrival times
    arrival_times.sort()
    
    total_time = 0
    current_bridge_end_time = arrival_times[0] + 20  # First boat starts immediately
    
    for i in range(n):
        if arrival_times[i] > current_bridge_end_time:
            # Boat must wait, update the end time of the bridge
            current_bridge_end_time = arrival_times[i] + 20
        else:
            # Boat passes immediately, update the end time of the bridge
            current_bridge_end_time += 20
        
        # Update the total time the bridge is unavailable
        if i < n - 1:
            next_boat_arrival = arrival_times[i + 1]
            wait_time = current_bridge_end_time - arrival_times[i]
            if wait_time > 30 * 60:  # Convert to seconds
                total_time += next_boat_arrival - (current_bridge_end_time - 20)
                current_bridge_end_time = next_boat_arrival + 20
            else:
                total_time += wait_time
    
    return total_time

# Read input
import sys
input = sys.stdin.read
data = input().split()
N = int(data[0])
arrival_times = [int(time) for time in data[1:]]

# Calculate and output the result
result = calculate_bridge_unavailability(arrival_times)
print(result)