def read_ints():
    return list(map(int, input().split()))

while True:
    N, M = read_ints()
    if N == 0 and M == 0:
        break
    
    calls = []
    for _ in range(N):
        source, destination, start, duration = read_ints()
        calls.append((start, start + duration))
    
    intervals = []
    for _ in range(M):
        start, duration = read_ints()
        intervals.append((start, start + duration))
    
    # Sort the calls and intervals by their start time
    calls.sort()
    intervals.sort()
    
    call_index = 0
    result = []
    
    for interval in intervals:
        count = 0
        start, end = interval
        while call_index < N and calls[call_index][0] <= start:
            if not (calls[call_index][1] < start or calls[call_index][0] > end):
                count += 1
            call_index += 1
        result.append(count)
    
    for r in result:
        print(r)