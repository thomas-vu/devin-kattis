Here's the Python code to solve the described problem:

```python
import sys

# Read input from stdin
N, Q = map(int, sys.stdin.readline().split())
tracks = [0] * (N + 1)
ans_queries = []

# Process each query
for _ in range(Q):
    query = list(map(int, sys.stdin.readline().split()))
    if query[0] == 1:
        # Place a LEGO track from si to ei
        _, si, ei = query
        tracks[si] += 1
        if ei + 1 <= N:
            tracks[ei + 1] -= 1
    else:
        # Query the total number of bullet points covered by at least one LEGO track
        ans = 0
        for i in range(1, N + 1):
            tracks[i] += tracks[i - 1]
            if tracks[i] > 0:
                ans += 1
        ans_queries.append(ans)

# Output the results for all query type 2
for ans in ans_queries:
    print(ans)