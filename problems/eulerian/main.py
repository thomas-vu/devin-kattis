def read_ints():
    return list(map(int, input().split()))

N, M = read_ints()
edges = [read_ints() for _ in range(M)]

# Create adjacency lists for the graph
graph = {i: [] for i in range(1, N + 1)}
in_degree = {i: 0 for i in range(1, N + 1)}
out_degree = {i: 0 for i in range(1, N + 1)}

# Build the graph and calculate degrees
for a, b in edges:
    graph[a].append(b)
    out_degree[a] += 1
    in_degree[b] += 1

# Check for Eulerian path conditions
start_nodes = end_nodes = 0
for i in range(1, N + 1):
    if out_degree[i] != in_degree[i]:
        if out_degree[i] == in_degree[i] + 1:
            end_nodes += 1
        elif in_degree[i] == out_degree[i] + 1:
            start_nodes += 1
        else:
            print("no")
            exit()

if start_nodes == 0 and end_nodes == 0:
    print("anywhere")
elif start_nodes == 1 and end_nodes == 1:
    print("specific")
else:
    print("no")