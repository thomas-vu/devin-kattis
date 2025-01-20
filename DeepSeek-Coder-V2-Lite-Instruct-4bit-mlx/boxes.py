import sys
from collections import defaultdict

# Read input
N = int(sys.stdin.readline().strip())
boxes = list(map(int, sys.stdin.readline().strip().split()))
Q = int(sys.stdin.readline().strip())
queries = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(Q)]

# Build the tree structure
parents = defaultdict(list)
for i in range(N):
    if boxes[i] != 0:
        parents[boxes[i]].append(i + 1)

# Function to count the number of boxes in a subtree
def count_boxes(node):
    count = 1
    for child in parents[node]:
        count += count_boxes(child)
    return count

# Process each query
for query in queries:
    indices = query[1:]
    total_count = 0
    for index in indices:
        if boxes[index - 1] != 0:
            total_count += count_boxes(index)
    print(total_count)