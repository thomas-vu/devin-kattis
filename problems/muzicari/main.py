def schedule_breaks(T, N, breaks):
    # Sort the breaks in ascending order to prioritize shorter breaks first
    breaks.sort()
    
    # Initialize the result list for the stage time of each musician
    stage_times = [0] * N
    
    # Iterate over each break time and assign the stage time accordingly
    for i in range(N):
        # Calculate the total available minutes up to this musician's break
        for j in range(i + 1):
            stage_times[i] += min(T - breaks[j], T // (N - j))
    
    return stage_times

# Read input
T, N = map(int, input().split())
breaks = list(map(int, input().split()))

# Get the stage times for each musician
stage_times = schedule_breaks(T, N, breaks)

# Output the result
for time in stage_times:
    print(time, end=' ')