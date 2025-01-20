def min_committees(n, enemies):
    graph = {i: [] for i in range(1, n + 1)}
    for a, b in enemies:
        graph[a].append(b)
        graph[b].append(a)
    
    colors = [-1] * (n + 1)
    
    def dfs(node, color):
        colors[node] = color
        for neighbor in graph[node]:
            if colors[neighbor] == -1:
                dfs(neighbor, 1 - color)
    
    for i in range(1, n + 1):
        if colors[i] == -1:
            dfs(i, 0)
    
    num_committees = sum(colors[i] == 1 for i in range(1, n + 1))
    return max(num_committees, 1)

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    enemies = []
    for _ in range(m):
        a, b = input().split()
        enemies.append((int(a), int(b)))
    print(min_committees(n, enemies))