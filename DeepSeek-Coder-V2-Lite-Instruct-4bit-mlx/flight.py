def read_ints():
    return list(map(int, input().split()))

n = int(input())
flights = [read_ints() for _ in range(n - 1)]

# Build the graph and find the diameter of the tree
graph = [[] for _ in range(n + 1)]
for a, b in flights:
    graph[a].append(b)
    graph[b].append(a)

def bfs(start):
    visited = [False] * (n + 1)
    distance = [-1] * (n + 1)
    queue = [start]
    visited[start] = True
    distance[start] = 0
    while queue:
        node = queue.pop(0)
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                distance[neighbor] = distance[node] + 1
                queue.append(neighbor)
    max_distance = max(distance[1:])
    farthest_node = distance.index(max_distance)
    return farthest_node, max_distance

# Find the diameter of the tree
farthest_node, _ = bfs(1)
_, max_distance = bfs(farthest_node)
diameter = max_distance

# Find the edges to remove and add to minimize flight changes
parent = [0] * (n + 1)
distance_from_root = [0] * (n + 1)
bfs_queue = [1]
visited = [False] * (n + 1)
visited[1] = True
while bfs_queue:
    node = bfs_queue.pop(0)
    for neighbor in graph[node]:
        if not visited[neighbor]:
            visited[neighbor] = True
            parent[neighbor] = node
            distance_from_root[neighbor] = distance_from_root[node] + 1
            bfs_queue.append(neighbor)

# Find the middle node of the diameter
middle_node = farthest_node
for _ in range(diameter // 2):
    middle_node = parent[middle_node]

# Find the edges to remove and add
if diameter % 2 == 0:
    node1 = parent[middle_node]
    node2 = middle_node
else:
    node1 = parent[middle_node]
    node2 = parent[parent[middle_node]]

# Output the result
print(diameter + 1)
print(node1, node2)
print(flights[0][0], flights[0][1])