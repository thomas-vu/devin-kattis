import sys
from math import log2, ceil

# Read the number of attractions from standard input
n = int(sys.stdin.readline().strip())

# Initialize adjacency list for the tree and a list to store degrees of nodes
adj_list = [[] for _ in range(n + 1)]
degree = [0] * (n + 1)

# Read the edges and populate the adjacency list and degree list
for _ in range(n - 1):
    i, j = map(int, sys.stdin.readline().strip().split())
    adj_list[i].append(j)
    degree[j] += 1

# Function to calculate the sum of path lengths for each node
def calc_path_lengths(node, parent):
    sum_length = 0
    count = [1] * (n + 1)  # Initialize counts for each node
    depths = [0] * (n + 1)  # Initialize depths for each node
    
    for child in adj_list[node]:
        if child != parent:
            depths[child] = depths[node] + 1
            sub_sum, sub_count = calc_path_lengths(child, node)
            count[node] += sub_count
            sum_length += sub_sum + sub_count
    
    # Calculate the path lengths for all multiples of node's label up to n
    paths = [0] * (n + 1)
    for i in range(node, n + 1, node):
        paths[i] = count[node] * (depths[node] + 1)
        for child in adj_list[node]:
            if child != parent:
                paths[i] += count[child] * (depths[node] + depths[child] + 1)
    
    # Update the sum of path lengths for each node
    total_sum = sum(paths[node:])
    
    return total_sum, count[node]

# Calculate the sum of path lengths from node 1
total_sum, _ = calc_path_lengths(1, -1)

# Output the result
print(total_sum)