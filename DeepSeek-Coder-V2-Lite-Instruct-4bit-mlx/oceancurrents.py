# This solution uses Dijkstra's algorithm to find the shortest path in a grid with weighted edges
# representing the current flow directions. The solution is implemented in Python 3.

import heapq

def dijkstra(grid, rows, cols):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    pq = [(0, rows-1, cols-1)]  # (cost, row, col)
    cost = [[float('inf')] * cols for _ in range(rows)]
    cost[rows-1][cols-1] = 0
    
    while pq:
        current_cost, x, y = heapq.heappop(pq)
        
        if (x, y) == (0, 0):
            return current_cost
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols:
                next_cost = current_cost + (0 if grid[nx][ny] == 0 else 1)
                if next_cost < cost[nx][ny]:
                    cost[nx][ny] = next_cost
                    heapq.heappush(pq, (next_cost, nx, ny))
    
    return float('inf')

def main():
    r, c = map(int, input().split())
    grid = [list(map(int, list(input().strip()))) for _ in range(r)]
    n = int(input())
    
    for _ in range(n):
        rs, cs, rd, cd = map(int, input().split())
        start = (r - rs, cs - 1)
        end = (rd - 1, cd - 1)
        result = dijkstra(grid, r, c)
        print(result)

if __name__ == "__main__":
    main()