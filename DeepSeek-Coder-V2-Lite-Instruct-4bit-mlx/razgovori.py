def min_phone_calls(N, M, detectors):
    left = 1
    right = M - 1
    min_calls = float('inf')
    
    while left <= right:
        mid = (left + right) // 2
        total_calls = 0
        
        for P, C in detectors:
            if P <= mid < P + C:
                total_calls += (P + C - 1) - mid
            elif P > mid:
                total_calls += (P + C - 1) - (mid + 1) + 1
        
        min_calls = min(min_calls, total_calls)
        
        if mid == (left + right) // 2:
            break
        
        if total_calls > N * (mid - left + 1):
            right = mid - 1
        else:
            left = mid + 1
    
    return min_calls

# Read input
N, M = map(int, input().split())
detectors = [tuple(map(int, input().split())) for _ in range(N)]

# Output the result
print(min_phone_calls(N, M, detectors))