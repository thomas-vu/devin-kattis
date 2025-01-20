def dfs(graph, dam, capacity_needed):
    downstream = graph[dam]
    if downstream == 0:
        return (capacity_needed, 0)
    
    capacity_remaining = downstream['capacity'] - downstream['water']
    if capacity_needed <= capacity_remaining:
        return (0, capacity_needed)
    else:
        excess = capacity_needed - capacity_remaining
        result = dfs(graph, downstream['downstream'], excess)
        return (result[0], result[1] + capacity_remaining)

n, w = map(int, input().split())
graph = {}
for i in range(n):
    downstream, capacity, water = map(int, input().split())
    graph[i + 1] = {'downstream': downstream, 'capacity': capacity, 'water': water}

min_rain = float('inf')
for i in range(n + 1):
    if i == 0:
        capacity_needed = w
    else:
        capacity_needed = graph[i]['capacity'] - graph[i]['water']
    result = dfs(graph, i, capacity_needed)
    min_rain = min(min_rain, result[0] + result[1])

print(min_rain)