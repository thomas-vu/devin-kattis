import heapq

def dijkstra(graph, start, n):
    distances = [float('inf')] * (n + 1)
    distances[start] = 0
    pq = [(0, start)]
    
    while pq:
        dist, node = heapq.heappop(pq)
        if dist > distances[node]:
            continue
        for neighbor, weight in graph[node]:
            new_dist = dist + weight
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))
    return distances

def main():
    n, m, t, d = map(int, input().split())
    repair_stations = list(map(int, input().split()))
    
    graph = {i: [] for i in range(1, n + 1)}
    
    for _ in range(m):
        i, j, k = map(int, input().split())
        graph[i].append((j, k))
        graph[j].append((i, k))
    
    # Run Dijkstra's from school (intersection 1) and home (intersection n)
    dist_from_school = dijkstra(graph, 1, n)
    dist_from_home = dijkstra(graph, n, n)
    
    min_distance = float('inf')
    
    # Check all repair stations and intersections to find the minimum distance
    for station in repair_stations:
        if dist_from_school[station] + dist_from_home[station] < min_distance:
            min_distance = dist_from_school[station] + dist_from_home[station]
    
    if min_distance <= d:
        print(min_distance)
    else:
        print("stuck")

if __name__ == "__main__":
    main()