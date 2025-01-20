def min_trips(n, m, weights):
    weights.sort()
    trips = 0
    left = 0
    right = n - 1
    
    while left <= right:
        if weights[left] + weights[right] <= m:
            left += 1
            right -= 1
        else:
            right -= 1
        trips += 1
    
    return trips

# Read input
n, m = map(int, input().split())
weights = list(map(int, input().split()))

# Calculate and print the result
print(min_trips(n, m, weights))