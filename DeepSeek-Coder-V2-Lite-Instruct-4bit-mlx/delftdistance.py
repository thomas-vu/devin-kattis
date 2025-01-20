import sys
from heapq import heappop, heappush

def shortest_path(h, w, grid):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = [[False] * w for _ in range(h)]
    heap = [(0, 0, 0)]  # (distance, x, y)
    
    while heap:
        dist, x, y = heappop(heap)
        
        if visited[x][y]:
            continue
        visited[x][y] = True
        
        if (x, y) == (h - 1, w - 1):
            return dist
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < h and 0 <= ny < w:
                if not visited[nx][ny]:
                    if grid[nx][ny] == 'O':
                        heappush(heap, (dist + 10 * 1.41421356237, nx, ny))
                    else:  # 'X'
                        heappush(heap, (dist + 10, nx, ny))
    
    return float('inf')

def main():
    input_line = sys.stdin.readline().strip()
    h, w = map(int, input_line.split())
    grid = [sys.stdin.readline().strip() for _ in range(h)]
    
    result = shortest_path(h, w, grid)
    print("{:.10f}".format(result))

if __name__ == "__main__":
    main()