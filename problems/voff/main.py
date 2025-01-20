def min_dogs(n, k, times):
    dogs = 1
    last_bark = times[0]
    
    for i in range(1, n):
        if times[i] - last_bark >= k + 1:
            dogs += 1
            last_bark = times[i]
    
    return dogs

# Read input
n, k = map(int, input().split())
times = list(map(int, input().split()))

# Calculate and print the result
print(min_dogs(n, k, times))