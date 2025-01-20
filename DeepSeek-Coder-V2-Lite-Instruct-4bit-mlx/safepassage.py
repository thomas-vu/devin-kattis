import sys

def min_time_to_dorm(times):
    N = len(times)
    # Create a bitmask to represent the state of who has crossed the campus
    all_crossed = (1 << N) - 1
    # Initialize a DP array where dp[mask] represents the minimum time to reach dorm with people represented by mask
    dp = [float('inf')] * (1 << N)
    # Base case: when no one has crossed, the time is 0
    dp[0] = 0
    
    for mask in range(1 << N):
        # Count the number of people who have crossed
        num_crossed = bin(mask).count('1')
        # For each pair of people, calculate the time if they cross together
        for i in range(N):
            if mask & (1 << i) == 0:  # If person i hasn't crossed
                for j in range(i + 1, N):
                    if mask & (1 << j) == 0:  # If person j hasn't crossed
                        new_mask = mask | (1 << i) | (1 << j)
                        # Calculate the time for pair (i, j) to cross
                        if num_crossed % 2 == 0:  # If it's an even step, they cross together
                            dp[new_mask] = min(dp[new_mask], max(times[i], times[j]) + dp[mask])
                        else:  # If it's an odd step, person i returns with the cloak
                            dp[new_mask] = min(dp[new_mask], times[i] + max(times[j], dp[mask]))
    return dp[all_crossed]

# Read input from stdin
input_line = sys.stdin.readline().strip()
N, *times = map(int, input_line.split())

# Calculate and output the minimum time to get everyone to the dorm
print(min_time_to_dorm(times))