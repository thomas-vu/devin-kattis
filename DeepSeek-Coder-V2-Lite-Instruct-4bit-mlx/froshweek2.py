def max_tasks(n, m, tasks, quiet_intervals):
    # Sort the lists of task durations and quiet intervals by their end times
    tasks.sort()
    quiet_intervals.sort()
    
    # Initialize pointers and count of tasks completed
    task_ptr = 0
    quiet_ptr = 0
    count = 0
    
    # Use two pointers to find the maximum number of tasks that can be completed
    while task_ptr < n and quiet_ptr < m:
        if tasks[task_ptr] <= quiet_intervals[quiet_ptr]:
            count += 1
            task_ptr += 1
        quiet_ptr += 1
    
    return count

# Read input
import sys
input = sys.stdin.read
data = input().split()
n = int(data[0])
m = int(data[1])
tasks = list(map(int, data[2:2+n]))
quiet_intervals = list(map(int, data[2+n:]))

# Calculate and output the result
result = max_tasks(n, m, tasks, quiet_intervals)
print(result)