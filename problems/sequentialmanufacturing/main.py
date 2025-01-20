def min_time_to_manufacture(N, P, processing_times, input_areas):
    # Initialize the time for each machine to process one item
    times = [0] * N
    
    # Process each item through the machines
    for _ in range(P):
        # For each machine, calculate the time to process the next item
        for i in range(N):
            if times[i] == 0:
                # If the machine is free, start processing a new item
                times[i] = processing_times[i]
            else:
                # If the machine is busy, wait for it to finish processing the current item
                times[i] += processing_times[i]
        
        # Check if the system can shut down after processing each item
        for i in range(N - 1):
            if times[i] > processing_times[i + 1]:
                # If the next machine is still busy, keep processing items
                break
        else:
            # If we reach this point, the system can shut down after processing each item
            return max(times)
    
    # Return the time when the last machine finishes processing the last item
    return max(times)

# Read input from stdin
import sys
input_data = sys.stdin.read().splitlines()
N, P = map(int, input_data[0].split())
processing_times = list(map(int, input_data[1].split()))
input_areas = list(map(int, input_data[2].split()))

# Calculate and output the minimum time to manufacture all items
result = min_time_to_manufacture(N, P, processing_times, input_areas)
print(result)