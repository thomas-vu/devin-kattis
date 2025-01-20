def find_smallest_difference(n, k, batteries):
    batteries.sort()
    min_diff = float('inf')
    
    for i in range(len(batteries) - (n * k - 1)):
        for j in range(i + n * k - 1, len(batteries)):
            diff = batteries[j] - batteries[i]
            min_diff = min(min_diff, diff)
    
    return min_diff

# Read input
n, k = map(int, input().split())
batteries = list(map(int, input().split()))

# Calculate and output the result
d = find_smallest_difference(n, k, batteries)
print(d)