def min_time(N, times):
    # Sort the teams based on their implementation time in ascending order
    sorted_times = sorted(times)
    
    # Initialize the total time needed for Ante and Goran to lecture all teams
    total_time = 0
    
    # Assign lectures to Ante and Goran in a balanced manner
    for i in range(N):
        total_time = max(total_time, sorted_times[i] + sorted_times[N - 1 - i])
    
    return total_time

# Read input
N = int(input())
times = list(map(int, input().split()))

# Calculate and print the minimum time required for both Ante and Goran to lecture all teams
print(min_time(N, times))