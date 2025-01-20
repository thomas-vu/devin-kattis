def read_ints():
    return list(map(int, input().split()))

# Read the number of junctions, producers, and conveyor belts
N, K, M = read_ints()

# Read the directed edges (conveyor belts)
edges = [read_ints() for _ in range(M)]

# Create adjacency list to represent the graph
adj_list = [[] for _ in range(N + 1)]
for a, b in edges:
    adj_list[a].append(b)

# Initialize the maximum number of producers that can be left running
max_producers = 0

# Try to turn off each producer and check the maximum number of producers that can still produce
for mask in range(1 << K):
    # Check if the current configuration is valid
    valid = True
    for i in range(K):
        if mask & (1 << i):  # Producer i is turned off
            start = i + 1
            current_junction = adj_list[start][0]
            while len(adj_list[current_junction]) == 1:
                current_junction = adj_list[current_junction][0]
            if current_junction != N:  # The producer's products are not delivered to the warehouse
                valid = False
                break
    if valid:
        # Count the number of producers that are still running in this configuration
        count = bin(mask).count('1')
        max_producers = max(max_producers, count)

# Output the maximum number of producers that can be left running
print(max_producers)