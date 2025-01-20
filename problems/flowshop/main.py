def min_time_to_complete(N, M, processing_times):
    # Initialize the completion times for each swather
    completion_times = [0] * N
    
    # Process each stage for each swather
    for j in range(M):
        for i in range(N):
            # Update the completion time for each swather based on the current stage
            if j == 0:
                completion_times[i] = processing_times[i][j]
            else:
                completion_times[i] = max(completion_times[i], completion_times[i-1]) + processing_times[i][j]
    
    return completion_times

# Read input
N, M = map(int, input().split())
processing_times = [list(map(int, input().split())) for _ in range(N)]

# Calculate the completion times
completion_times = min_time_to_complete(N, M, processing_times)

# Output the result
print(' '.join(map(str, completion_times)))