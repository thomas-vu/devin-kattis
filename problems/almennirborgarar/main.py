def min_waiting_time(n, m, grills):
    # Sort the grills by their cooking time in ascending order
    sorted_grills = sorted(grills)
    
    # Initialize the waiting times for each grill
    waiting_times = [0] * n
    
    # Process the burgers in a round-robin fashion using the grills
    for i in range(m):
        # Assign a burger to the grill that finishes first
        min_index = 0
        for j in range(1, n):
            if waiting_times[j] < waiting_times[min_index]:
                min_index = j
        # Update the waiting time for the assigned grill
        waiting_times[min_index] += sorted_grills[min_index]
    
    # The total waiting time for Benni is the maximum of all waiting times
    return max(waiting_times)

# Read input
n, m = map(int, input().split())
grills = list(map(int, input().split()))

# Calculate and print the result
print(min_waiting_time(n, m, grills))