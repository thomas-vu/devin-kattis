import sys

n = int(input())
edges_count = [0] * (n + 1)
for i in range(2, n + 1):
    print("? {} {}".format(i, end=''))
    sys.stdout.flush()
    edges = int(input())
    edges_count[i] = edges
    edges_count[i - 1] = n - i + 1 - edges

adj_matrix = [[0] * n for _ in range(n)]
for i in range(1, n):
    for j in range(i + 1, n + 1):
        if edges_count[i] + edges_count[j] == edges_count[n]:
            adj_matrix[i - 1][j - 1] = 1
            adj_matrix[j - 1][i - 1] = 1

print("!")
for row in adj_matrix:
    print(' '.join(map(str, row)))