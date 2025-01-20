import sys
from bisect import bisect_left, bisect_right

# Read input from stdin
N = int(sys.stdin.readline().strip())
items = [tuple(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
Q = int(sys.stdin.readline().strip())
queries = [tuple(map(int, sys.stdin.readline().strip().split())) for _ in range(Q)]

# Process each query
for X, K in queries:
    # Filter items based on the value condition
    filtered_items = [i for i, (P, V) in enumerate(items) if V <= X]
    
    # Sort the filtered items based on value and index
    sorted_items = sorted(filtered_items, key=lambda i: (-items[i][0], i))
    
    # Get the best K items indices
    if len(sorted_items) >= K:
        result = sorted_items[:K]
    else:
        result = sorted_items if sorted_items else [-1]
    
    # Output the result
    print(" ".join(map(str, result)))