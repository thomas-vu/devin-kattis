import sys
from collections import defaultdict

def read_ints():
    return list(map(int, input().split()))

def solve(f, i, stations, edges):
    graph = defaultdict(list)
    for a, b, w in edges:
        graph[a].append((b, w))
        graph[b].append((a, w))
    
    # Dijkstra's algorithm to find the shortest path from each intersection to the nearest fire station
    def dijkstra(start):
        import heapq
        dist = [float('inf')] * (i + 1)
        dist[start] = 0
        pq = [(0, start)]
        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[u]:
                continue
            for v, w in graph[u]:
                if dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w
                    heapq.heappush(pq, (dist[v], v))
        return dist
    
    # Initialize the minimum distance to a large number
    min_dist = float('inf')
    best_location = -1
    
    # Check each intersection for the new fire station location
    for start in range(1, i + 1):
        dist = dijkstra(start)
        max_dist = max([min(dist[u], dist[v]) for u, v in edges])
        if max_dist < min_dist:
            min_dist = max_dist
            best_location = start
    
    return best_location

def main():
    input_lines = sys.stdin.read().splitlines()
    index = 0
    t = int(input_lines[index])
    index += 1
    for _ in range(t):
        if _ > 0:
            input()
        f, i = read_ints()
        stations = set(read_ints())
        edges = []
        while index < len(input_lines) and input_lines[index].strip():
            a, b, w = read_ints()
            edges.append((a, b, w))
            index += 1
        result = solve(f, i, stations, edges)
        print(result)
        index += 1
        if index < len(input_lines):
            input()

if __name__ == "__main__":
    main()