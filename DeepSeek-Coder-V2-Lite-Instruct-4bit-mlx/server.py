def max_tasks(n, T, task_times):
    time_spent = 0
    tasks_completed = 0
    
    for task_time in task_times:
        if time_spent + task_time <= T:
            time_spent += task_time
            tasks_completed += 1
        else:
            break
    
    return tasks_completed

# Read input
n, T = map(int, input().split())
task_times = list(map(int, input().split()))

# Calculate and output the result
print(max_tasks(n, T, task_times))