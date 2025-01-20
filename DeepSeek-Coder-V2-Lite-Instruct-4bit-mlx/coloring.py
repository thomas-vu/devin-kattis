def min_colors(graph):
    N = len(graph)
    color_count = [0] * N
    
    def dfs(v, c):
        color_count[c] += 1
        for u in graph[v]:
            if color_count[c] > 1:
                continue
            dfs(u, c)
    
    for i in range(N):
        if color_count[i] == 0:
            dfs(i, i)
    
    return max(color_count)

# Read input
N = int(input())
graph = [[] for _ in range(N)]
for i in range(N):
    edges = list(map(int, input().split()[1:]))
    for j in edges:
        graph[i].append(j)
        graph[j].append(i)

# Output the result
print(min_colors(graph))