def min_max_total_size(N, M, items):
    # Sort the items to make it easier to find pairs that sum up to the smallest possible total size
    items.sort()
    
    # Initialize variables to store the best configuration found so far
    min_max_total = float('inf')
    
    # Iterate through all possible pairs of items to find the smallest total size for any scout
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):  # Ensure no more than two items per scout
                total_size = items[i] + items[j] + items[k]
                min_max_total = min(min_max_total, total_size)
    
    return min_max_total

# Read input from stdin
import sys
input = sys.stdin.read
data = input().split()

# Parse the data
N = int(data[0])
M = int(data[1])
items = list(map(int, data[2:]))

# Get the result and print it
result = min_max_total_size(N, M, items)
print(result)