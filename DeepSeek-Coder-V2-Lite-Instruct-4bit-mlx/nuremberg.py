def dfs(graph, node, visited):
    visited[node] = True
    total_time = 0
    for neighbor, weight in graph[node]:
        if not visited[neighbor]:
            total_time += weight + dfs(graph, neighbor, visited)
    return total_time

def main():
    c = int(input())
    for _ in range(c):
        n = int(input())
        graph = {i: [] for i in range(1, n + 1)}
        for _ in range(n - 1):
            a, b, t = map(int, input().split())
            graph[a].append((b, t))
            graph[b].append((a, t))
        
        m = int(input())
        freq = {}
        for _ in range(m):
            a, f = map(int, input().split())
            freq[a] = f
        
        min_time = float('inf')
        optimal_stations = []
        
        for start in range(1, n + 1):
            visited = [False] * (n + 1)
            total_time = dfs(graph, start, visited)
            
            if total_time < min_time:
                min_time = total_time
                optimal_stations = [start]
            elif total_time == min_time:
                optimal_stations.append(start)
        
        total_traffic_time = 0
        for station in optimal_stations:
            visited = [False] * (n + 1)
            total_traffic_time += dfs(graph, station, visited) * sum(freq.values())
        
        print(total_traffic_time)
        print(' '.join(map(str, sorted(optimal_stations))))

if __name__ == "__main__":
    main()