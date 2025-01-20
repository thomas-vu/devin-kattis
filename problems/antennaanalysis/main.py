def significant_differences(n, c, measurements):
    y = [0] * n
    max_diff = 0
    
    for i in range(n):
        current_max = float('-inf')
        for j in range(i):
            diff = abs(measurements[i] - measurements[j]) - c * (i - j)
            current_max = max(current_max, diff)
        y[i] = current_max
    
    return y

# Read input
n, c = map(int, input().split())
measurements = list(map(int, input().split()))

# Calculate and print the result
result = significant_differences(n, c, measurements)
print(' '.join(map(str, result)))