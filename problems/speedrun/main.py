def can_complete_tasks(G, N, tasks):
    # Sort the tasks by their start time
    tasks.sort(key=lambda x: x[0])
    
    # Initialize the time when the last task ended
    end_time = 0
    
    # Iterate through each task
    for start, end in tasks:
        if start >= end_time:
            # If the current task can be started, update the end time
            end_time = end
        else:
            # If not, we cannot complete all tasks on the first day
            return "NO"
    # Check if we have completed at least G tasks
    if end_time >= 24000:
        return "NO"
    else:
        return "YES"

# Read input
G, N = map(int, input().split())
tasks = [tuple(map(int, input().split())) for _ in range(N)]

# Output the result
print(can_complete_tasks(G, N, tasks))