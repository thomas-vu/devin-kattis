import heapq

def euclidean_distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

def dijkstra(graph, start, end):
    n = len(graph)
    dist = [float('inf')] * n
    prev = [-1] * n
    dist[start] = 0
    pq = [(0, start)]
    
    while pq:
        d, u = heapq.heappop(pq)
        if u == end:
            break
        for v, weight in graph[u]:
            new_dist = d + weight
            if new_dist < dist[v]:
                dist[v] = new_dist
                prev[v] = u
                heapq.heappush(pq, (new_dist, v))
    
    path = []
    u = end
    while u != -1:
        path.append(u)
        u = prev[u]
    return dist[end], list(reversed(path))

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    N = int(data[index])
    M = int(data[index + 1])
    index += 2
    
    places = []
    for _ in range(N):
        x = int(data[index])
        y = int(data[index + 1])
        floor = int(data[index + 2])
        index += 3
        places.append((floor, x, y))
    
    graph = [[] for _ in range(N)]
    for _ in range(M):
        u = int(data[index])
        v = int(data[index + 1])
        movement_type = data[index + 2]
        weight = 0
        if movement_type == 'walking':
            floor1, x1, y1 = places[u]
            floor2, x2, y2 = places[v]
            weight = euclidean_distance(x1, y1, x2, y2)
        elif movement_type == 'stairs':
            weight = euclidean_distance(places[u][1], places[u][2], places[v][1], places[v][2])
        elif movement_type == 'lift':
            weight = 1
        elif movement_type == 'escalator':
            floor1, x1, y1 = places[u]
            floor2, x2, y2 = places[v]
            if (floor1 < floor2 and euclidean_distance(x1, y1, x2, y2) == 0) or (floor1 > floor2 and euclidean_distance(x1, y1, x2, y2) == 0):
                weight = euclidean_distance(x1, y1, x2, y2)
            else:
                weight = euclidean_distance(x1, y1, x2, y2) * 3
        index += 3
        graph[u].append((v, weight))
        graph[v].append((u, weight))
    
    Q = int(data[index])
    index += 1
    for _ in range(Q):
        a = int(data[index])
        b = int(data[index + 1])
        index += 2
        dist, path = dijkstra(graph, a, b)
        print(*path)

if __name__ == "__main__":
    main()