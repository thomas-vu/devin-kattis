import sys
from math import inf
from heapq import heappush, heappop

def dijkstra(graph, start):
    n = len(graph)
    m = len(graph[0])
    dist = [[inf for _ in range(m)] for _ in range(n)]
    dist[start[0]][start[1]] = 0
    pq = [(0, start)]
    
    while pq:
        d, (x, y) = heappop(pq)
        if d > dist[x][y]:
            continue
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] != '#' and dist[nx][ny] > d + 1:
                dist[nx][ny] = d + 1
                heappush(pq, (dist[nx][ny], (nx, ny)))
    return dist

def main():
    L, W = map(int, sys.stdin.readline().strip().split())
    cave_map = [sys.stdin.readline().strip() for _ in range(L)]
    start_x, start_y = -1, -1
    diamond_x, diamond_y = -1, -1
    
    for i in range(L):
        for j in range(W):
            if cave_map[i][j] == 'E':
                start_x, start_y = i, j
            elif cave_map[i][j] == 'D':
                diamond_x, diamond_y = i, j
    
    graph = [[cave_map[i][j] for j in range(W)] for i in range(L)]
    dist = dijkstra(graph, (start_x, start_y))
    
    total_tiles = sum(row.count(' ') for row in cave_map)
    grue_encounter = 0
    
    for i in range(L):
        for j in range(W):
            if graph[i][j] == ' ':
                grue_encounter += 1
    
    probability = (total_tiles - dist[diamond_x][diamond_y]) / total_tiles
    print("{:.6f}".format(probability))

if __name__ == "__main__":
    main()