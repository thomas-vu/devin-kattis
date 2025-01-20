import heapq
import sys

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        if current_distance > distances[current_node]:
            continue
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    return distances

def count_routes(graph, n):
    start = 1
    end = 2
    distances_start = dijkstra(graph, start)
    distances_end = dijkstra(graph, end)
    
    count = 0
    for node in range(1, n + 1):
        if distances_start[node] < distances_end[2]:
            count += 1
    return count

def main():
    while True:
        line = sys.stdin.readline().strip()
        if line == '0':
            break
        n, m = map(int, line.split())
        graph = {i: {} for i in range(1, n + 1)}
        for _ in range(m):
            a, b, d = map(int, sys.stdin.readline().strip().split())
            graph[a][b] = d
            graph[b][a] = d
        print(count_routes(graph, n))

if __name__ == "__main__":
    main()