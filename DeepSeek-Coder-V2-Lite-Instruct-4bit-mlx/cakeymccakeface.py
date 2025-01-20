def find_secret_cooking_time(entry_times, exit_times):
    best_diff = 0
    max_count = 0
    
    for diff in range(1, 1000001):
        count = sum(1 for entry in entry_times if (entry + diff) in exit_times)
        if count > max_count:
            max_count = count
            best_diff = diff
        elif count == max_count and diff < best_diff:
            best_diff = diff
    
    return best_diff

# Read input
N = int(input())
M = int(input())
entry_times = list(map(int, input().split()))
exit_times = list(map(int, input().split()))

# Get the best guess of the secret cooking time
result = find_secret_cooking_time(entry_times, exit_times)
print(result)