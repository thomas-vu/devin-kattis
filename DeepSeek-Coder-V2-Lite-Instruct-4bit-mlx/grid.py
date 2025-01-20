# Dijkstra's algorithm adapted for the grid problem with jumps based on digits
import heapq

def min_moves(grid):
    n = len(grid)
    m = len(grid[0])
    
    # Directions for moving right, down, left, up
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    # Priority queue for Dijkstra's algorithm
    pq = [(0, 0, 0)]  # (distance, x, y)
    dist = [[float('inf')] * m for _ in range(n)]
    dist[0][0] = 0
    
    while pq:
        d, x, y = heapq.heappop(pq)
        
        # If reached the bottom-right corner
        if x == n - 1 and y == m - 1:
            return d
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                jump = int(grid[nx][ny])
                new_dist = d + 1
                
                # Check if the jump is valid and leads to a shorter path
                while new_dist < dist[nx][ny] and 0 <= nx + dx*jump < n and 0 <= ny + dy*jump < m:
                    nx, ny = nx + dx*jump, ny + dy*jump
                    new_dist += 1
                
                if new_dist < dist[nx][ny]:
                    dist[nx][ny] = new_dist
                    heapq.heappush(pq, (new_dist, nx, ny))
    
    return -1

# Read input
n, m = map(int, input().split())
grid = [input() for _ in range(n)]

# Output the minimum number of moves required
print(min_moves(grid))