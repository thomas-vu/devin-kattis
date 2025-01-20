def min_missed_seconds(N, T, S, breaks):
    missed = 0
    current_end = 0
    
    for l, r in breaks:
        if l > current_end:
            start = max(current_end, S)
            end = min(r, T - S + 1)
            missed += max(0, end - start)
        current_end = max(current_end, r)
    
    return missed

# Read input
N, T, S = map(int, input().split())
breaks = [tuple(map(int, input().split())) for _ in range(N)]

# Calculate and print the result
print(min_missed_seconds(N, T, S, breaks))