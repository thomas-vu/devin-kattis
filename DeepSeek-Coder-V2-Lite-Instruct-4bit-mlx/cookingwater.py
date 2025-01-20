def check_intervals(N, intervals):
    if N == 1:
        return "gunilla has a point"
    
    time_watched = set()
    for interval in intervals:
        a, b = interval
        time_watched.update(range(a, b + 1))
    
    if len(time_watched) == N:
        return "gunilla has a point"
    else:
        return "edward is right"

# Read input
N = int(input())
intervals = [tuple(map(int, input().split())) for _ in range(N)]

# Output the result
print(check_intervals(N, intervals))