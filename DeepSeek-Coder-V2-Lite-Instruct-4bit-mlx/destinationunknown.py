def find_possible_destinations(n, m, t, s, g, h, roads, destinations):
    graph = [[] for _ in range(n + 1)]
    for a, b, d in roads:
        graph[a].append((b, d))
        graph[b].append((a, d))
    
    def dijkstra(start):
        import heapq
        dist = [float('inf')] * (n + 1)
        dist[start] = 0
        pq = [(0, start)]
        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[u]:
                continue
            for v, w in graph[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    heapq.heappush(pq, (dist[v], v))
        return dist
    
    dist_s = dijkstra(s)
    dist_g = dijkstra(g)
    dist_h = dijkstra(h)
    
    min_distance = float('inf')
    possible_destinations = []
    for dest in destinations:
        path_gh = dist_g[h] + dist_h[dest]
        if dist_s[dest] == path_gh:
            possible_destinations.append(dest)
    possible_destinations.sort()
    return possible_destinations

# Read input
import sys
input = sys.stdin.read
lines = input().split('\n')
index = 0
test_cases = int(lines[index])
index += 1
results = []
for _ in range(test_cases):
    n, m, t = map(int, lines[index].split())
    index += 1
    s, g, h = map(int, lines[index].split())
    index += 1
    roads = []
    for _ in range(m):
        a, b, d = map(int, lines[index].split())
        roads.append((a, b, d))
        index += 1
    destinations = list(map(int, lines[index].split()))
    index += 1
    
    possible_destinations = find_possible_destinations(n, m, t, s, g, h, roads, destinations)
    results.append(' '.join(map(str, possible_destinations)))

# Output results
for result in results:
    print(result)