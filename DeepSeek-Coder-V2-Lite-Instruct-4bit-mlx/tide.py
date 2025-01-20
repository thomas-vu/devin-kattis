from heapq import heappop, heappush
import sys

input = sys.stdin.read
lines = input().split()
index = 0

def read_int():
    global index
    value = int(lines[index])
    index += 1
    return value

def read_ints():
    global index
    values = []
    while index < len(lines):
        values.append(int(lines[index]))
        index += 1
    return values

def read_float():
    global index
    value = float(lines[index])
    index += 1
    return value

def read_floats():
    global index
    values = []
    while index < len(lines):
        values.append(float(lines[index]))
        index += 1
    return values

def main():
    T = read_int()
    for t in range(1, T + 1):
        H = read_int()
        N = read_int()
        M = read_int()
        
        ceiling = []
        floor = []
        
        for _ in range(N):
            ceiling.append(read_ints())
        for _ in range(N):
            floor.append(read_ints())
        
        # Create a graph where each node represents a grid square
        # and edges represent possible moves between squares
        graph = [[{} for _ in range(M)] for _ in range(N)]
        
        for i in range(N):
            for j in range(M):
                if i > 0:
                    if ceiling[i-1][j] - floor[i][j] >= 50 and ceiling[i][j] - floor[i-1][j] >= 50:
                        graph[i][j][(i-1, j)] = 1 if ceiling[i][j] - (H - (i * 10)) >= 50 else 10
                if i < N - 1:
                    if ceiling[i+1][j] - floor[i][j] >= 50 and ceiling[i][j] - floor[i+1][j] >= 50:
                        graph[i][j][(i+1, j)] = 1 if ceiling[i][j] - (H - (i * 10)) >= 50 else 10
                if j > 0:
                    if ceiling[i][j-1] - floor[i][j] >= 50 and ceiling[i][j] - floor[i][j-1] >= 50:
                        graph[i][j][(i, j-1)] = 1 if ceiling[i][j] - (H - (i * 10)) >= 50 else 10
                if j < M - 1:
                    if ceiling[i][j+1] - floor[i][j] >= 50 and ceiling[i][j] - floor[i][j+1] >= 50:
                        graph[i][j][(i, j+1)] = 1 if ceiling[i][j] - (H - (i * 10)) >= 50 else 10
        
        # Dijkstra's algorithm to find the shortest path to the exit
        dist = [[float('inf') for _ in range(M)] for _ in range(N)]
        dist[0][0] = 0
        pq = [(0, 0, 0)] # (distance, x, y)
        
        while pq:
            d, x, y = heappop(pq)
            if (x, y) == (N - 1, M - 1):
                break
            for nx, ny in graph[x][y]:
                new_dist = d + graph[x][y][(nx, ny)]
                if new_dist < dist[nx][ny]:
                    dist[nx][ny] = new_dist
                    heappush(pq, (new_dist, nx, ny))
        
        result = dist[N-1][M-1] / 10.0 if dist[N-1][M-1] != float('inf') else 0.0
        print(f"Case #{t}: {result}")

if __name__ == "__main__":
    main()