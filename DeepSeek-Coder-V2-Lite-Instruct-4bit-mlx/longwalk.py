def count_edges(n, m, nodes):
    total_edges = 0
    for i in range(m - 1):
        u, v = nodes[i], nodes[i + 1]
        while u != v:
            if u < v:
                u, v = u * 2 % (1 << n), v
            else:
                u, v = u, v * 2 % (1 << n)
            total_edges += 1
    return total_edges

# Read input
import sys
input = sys.stdin.read
data = input().split()
n, m = int(data[0]), int(data[1])
nodes = list(map(int, data[2:]))

# Calculate and output the result
result = count_edges(n, m, nodes)
print(result)