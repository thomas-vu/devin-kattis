import sys
from heapq import heappop, heappush

def min_energy(N, M, L, S, initial_stations, edges):
    graph = {i: [] for i in range(1, N + 1)}
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    min_heap = []
    for station in initial_stations:
        heappush(min_heap, (0, station))
    
    dist = [float('inf')] * (N + 1)
    for station in initial_stations:
        dist[station] = 0
    
    while min_heap:
        d, u = heappop(min_heap)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            if dist[v] > d + w:
                dist[v] = d + w
                heappush(min_heap, (dist[v], v))
    
    total_energy = 0
    for i in range(1, N + 1):
        total_energy += dist[i] * L
    
    return total_energy

def main():
    input_data = sys.stdin.read().splitlines()
    dataset_count = int(input_data[0])
    
    index = 1
    results = []
    for _ in range(dataset_count):
        N, M, L, S = map(int, input_data[index].split())
        initial_stations = list(map(int, input_data[index + 1].split()))
        edges = []
        for i in range(index + 2, index + 2 + M):
            u, v, w = map(int, input_data[i].split())
            edges.append((u, v, w))
        index += 2 + M
        results.append(min_energy(N, M, L, S, initial_stations, edges))
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()