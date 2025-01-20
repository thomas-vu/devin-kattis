def min_hyper_tunnels(n, m, startA, startB, tunnels):
    from collections import defaultdict, deque
    
    graph = defaultdict(list)
    for p1, p2 in tunnels:
        graph[p1].append(p2)
        graph[p2].append(p1)
    
    def bfs(start):
        visited = set()
        queue = deque([(start, 0)])
        distance = {}
        while queue:
            planet, dist = queue.popleft()
            if planet in visited:
                continue
            visited.add(planet)
            distance[planet] = dist
            for neighbor in graph[planet]:
                if neighbor not in visited:
                    queue.append((neighbor, dist + 1))
        return distance
    
    distancesA = bfs(startA)
    distancesB = bfs(startB)
    
    max_distance = 0
    for planet in range(n):
        if planet in distancesA and planet in distancesB:
            max_distance = max(max_distance, min(distancesA[planet], distancesB[planet]))
    
    return max_distance

# Read input
n, m = map(int, input().split())
startA, startB = map(int, input().split())
tunnels = [tuple(map(int, input().split())) for _ in range(m)]

# Calculate and print the result
result = min_hyper_tunnels(n, m, startA, startB, tunnels)
print(result)