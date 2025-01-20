a, b = map(int, input().split('/'))
n = (a * 4) // b
m = n - 1
edges = []

for i in range(2, n + 1):
    edges.append((1, i))

for i in range(2, n):
    edges.append((i, i + 1))

print(n, len(edges))
for u, v in edges:
    print(u, v)