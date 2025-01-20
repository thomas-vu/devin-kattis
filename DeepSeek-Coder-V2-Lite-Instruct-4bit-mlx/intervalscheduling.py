def max_nonoverlapping_intervals(intervals):
    if not intervals:
        return 0
    
    # Sort intervals by their end times
    intervals.sort(key=lambda x: x[1])
    
    # Initialize the count of nonoverlapping intervals
    count = 0
    last_end = float('-inf')
    
    for interval in intervals:
        start, end = interval
        if start >= last_end:
            count += 1
            last_end = end
    
    return count

# Read input
n = int(input().strip())
intervals = [tuple(map(int, input().strip().split())) for _ in range(n)]

# Output the result
print(max_nonoverlapping_intervals(intervals))