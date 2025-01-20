import sys
from collections import defaultdict, deque

# Read input from stdin
input_lines = sys.stdin.read().splitlines()

# Parse input
index = 0
N, Q = map(int, input_lines[index].split())
index += 1
colours = list(map(int, input_lines[index].split()))
index += 1
parents = list(map(int, input_lines[index].split()))
queries = []
for _ in range(Q):
    K, X = map(int, input_lines[index].split())
    queries.append((K, X))
    index += 1

# Build the tree
tree = defaultdict(list)
for i in range(2, N + 1):
    tree[parents[i - 2]].append(i)

# Process queries
results = []
for K, X in queries:
    if K == 0:
        # Query for the number of magical colours in the subtree of node X
        def count_magical_colours(node):
            queue = deque([node])
            colour_count = defaultdict(int)
            while queue:
                current = queue.popleft()
                colour_count[colours[current - 1]] += 1
                for child in tree[current]:
                    queue.append(child)
            return sum(1 for count in colour_count.values() if count % 2 == 1)
        results.append(count_magical_colours(X))
    else:
        # Change the colour of node X to K
        colours[X - 1] = K

# Output the results
for result in results:
    print(result)