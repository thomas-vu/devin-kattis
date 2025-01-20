import sys
from math import inf

def floyd_warshall(dist):
    n = len(dist)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist

def main():
    n = int(input().strip())
    dist = [list(map(int, input().split())) for _ in range(n)]
    dist = floyd_warshall(dist)
    
    r = int(input().strip())
    times = [tuple(map(int, input().split())) for _ in range(r)]
    
    q = int(input().strip())
    queries = [tuple(map(int, input().split())) for _ in range(q)]
    
    min_time = {}
    max_time = {}
    
    for s, d, t in times:
        if (s, d) not in min_time:
            min_time[(s, d)] = t
            max_time[(s, d)] = t
        else:
            min_time[(s, d)] = min(min_time[(s, d)], t)
            max_time[(s, d)] = max(max_time[(s, d)], t)
    
    for s, d in queries:
        min_est = min_time.get((s, d), inf)
        max_est = max_time.get((s, d), inf)
        
        if dist[s][d] != -1:
            min_est = min(min_est, dist[s][d])
            max_est = max(max_est, dist[s][d])
        
        for i in range(n):
            if dist[s][i] != -1 and dist[i][d] != -1:
                travel_time = dist[s][i] + dist[i][d]
                min_est = min(min_est, travel_time)
                max_est = max(max_est, travel_time)
        
        print(f"{s} {d} {min_est/60:.1f} {max_est/60:.1f}")

if __name__ == "__main__":
    main()