import sys
from heapq import heappop, heappush

def min_sum_path(grid, X, Y, code_key):
    # Function to calculate the minimum sum path using Dijkstra's algorithm
    def dijkstra(start_x, start_y):
        # Directions for moving right and up
        directions = [(0, 1), (1, 0)]
        # Priority queue to store the nodes with their current path sum
        pq = [(0, start_x, start_y)]
        # Distance array to store the minimum path sum to each cell
        dist = [[sys.maxsize for _ in range(X)] for _ in range(Y)]
        dist[start_y][start_x] = 0
        
        while pq:
            current_dist, x, y = heappop(pq)
            
            # If we have reached the destination cell (X, Y)
            if x == X - 1 and y == Y - 1:
                return current_dist
            
            # Explore the neighboring cells
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < X and 0 <= ny < Y:
                    next_dist = current_dist + int(grid[ny][nx])
                    if next_dist < dist[ny][nx]:
                        dist[ny][nx] = next_dist
                        heappush(pq, (next_dist, nx, ny))
        return sys.maxsize
    
    # Read the code key and remove leading digits
    code_key = str(code_key)
    while code_key and int(code_key[0]) <= X + Y:
        hops = int(code_key[0])
        code_key = code_key[1:]
        start_x, start_y = 0, 0
        end_x, end_y = X - 1, Y - 1
    
    return dijkstra(start_x, start_y)

# Read input
X, Y = map(int, sys.stdin.readline().split())
code_key = int(sys.stdin.readline())
grid = [sys.stdin.readline().strip() for _ in range(Y)]

# Calculate and print the result
result = min_sum_path(grid, X, Y, code_key)
print(result)