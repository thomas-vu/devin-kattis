import sys
from math import log, ceil

# Read input from stdin
N, K, Q = map(int, sys.stdin.readline().split())
queries = [list(map(int, sys.stdin.readline().split())) for _ in range(Q)]

# Calculate the depth of each node
depth = [0] * (N + 1)
for i in range(2, N + 1):
    depth[i] = (depth[i - 1] + K - 1) // K

# Calculate the position of each node in its depth
position = [0] * (N + 1)
for i in range(1, N + 1):
    position[i] = (i - 1) % K

# Process each query
for x, y in queries:
    if depth[x] == depth[y]:
        # Same level, count the number of steps to reach y from x
        current = x
        steps = 0
        while current != y:
            current = (current + K) // K
            steps += 1
        print(steps)
    else:
        # Different levels, count the number of steps to reach y from x
        if depth[x] < depth[y]:
            x, y = y, x  # Ensure x is deeper than y
        steps_x_to_root = depth[x] - 1
        steps_y_to_root = depth[y] - 1
        x = (x - 1) // K + 1
        y = (y - 1) // K + 1
        while x != y:
            if x > y:
                x = (x - 1) // K + 1
            else:
                y = (y - 1) // K + 1
            steps_x_to_root += 1
            steps_y_to_root += 1
        print(steps_x_to_root + steps_y_to_root)