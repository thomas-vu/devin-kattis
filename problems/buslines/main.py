def solve(n, m):
    if m < n - 1 or m > (n * (n + 1)) // 2:
        print(-1)
        return
    edges = []
    for i in range(1, n):
        edges.append((i, i + 1))
    for i in range(n - m + edges.count((2, 1)), n):
        edges.append((1, i + 1))
    if len(edges) != m:
        print(-1)
        return
    for edge in edges:
        print(*edge)

# Read input
n, m = map(int, input().split())
solve(n, m)