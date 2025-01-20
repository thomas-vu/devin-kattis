def min_trips(n, p, trips):
    total = sum(trips)
    if total <= p:
        return n
    
    for i in range(n):
        if trips[i] > p:
            return 1
    
    left = min(trips)
    right = sum(trips)
    
    while left < right:
        mid = (left + right) // 2
        required_pages = sum(max(0, trip - mid) for trip in trips)
        if required_pages <= mid * (n - 1):
            right = mid
        else:
            left = mid + 1
    
    for i in range(n):
        trips[i] = max(0, trips[i] - left)
    
    required_pages = sum(trips)
    if required_pages <= left:
        return n - (left // sum(trips[0] for trips in [trips]))
    
    return n + 1

# Read input
n, p = map(int, input().split())
trips = [int(input()) for _ in range(n)]

# Output the result
print(min_trips(n, p, trips))