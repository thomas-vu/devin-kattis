import sys
from collections import defaultdict, deque

def read_ints():
    return list(map(int, sys.stdin.readline().strip().split()))

n = int(sys.stdin.readline().strip())
parents = read_ints()
flows = [0] + read_ints()

# Build the tree
tree = defaultdict(list)
for i in range(2, n + 1):
    tree[parents[i - 2]].append(i)

# Check if the tree is valid and collect unknown flows
unknown_flows = []
for i in range(1, n + 1):
    if flows[i] == 0:
        unknown_flows.append(i)

# Assign flows to leaves based on the known values from above
assigned_flows = {}
for leaf in unknown_flows:
    node = leaf
    while node != 1 and flows[node] == 0:
        parent = parents[node - 2]
        if flows[parent] != 0:
            assigned_flows[leaf] = flows[parent] - sum(assigned_flows.get(child, 0) for child in tree[node])
            break
        node = parent

# Check consistency of the assigned flows and propagate them down
queue = deque([1])
while queue:
    node = queue.popleft()
    known_flow = sum(assigned_flows.get(child, 0) for child in tree[node])
    if flows[node] != 0:
        if flows[node] != known_flow + (assigned_flows.get(node, 0) if node in assigned_flows else 0):
            print("impossible")
            sys.exit()
    else:
        flows[node] = known_flow + (assigned_flows.get(node, 0) if node in assigned_flows else 0)
    for child in tree[node]:
        queue.append(child)

# Output the reconstructed flows if possible
if all(flow != 0 for flow in flows):
    ordered_flows = sorted([flows[i] for i in range(1, n + 1) if flows[i] != 0])
    print("\n".join(map(str, ordered_flows)))
else:
    print("impossible")