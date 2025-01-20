def min_ladder_length(grid):
    M, N = len(grid), len(grid[0])
    
    # Create a distance matrix to store the minimum ladder length required to reach each cell
    dist = [[float('inf')] * N for _ in range(M)]
    dist[0][0] = 0
    
    # Directions for moving north, west, south, and east
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    
    # Priority queue to perform Dijkstra's algorithm
    import heapq
    pq = [(0, 0, 0)]  # (distance, x, y)
    
    while pq:
        d, x, y = heapq.heappop(pq)
        
        # If we reached the bottom-right corner, return the distance
        if x == M - 1 and y == N - 1:
            return d
        
        # Explore the neighbors
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < M and 0 <= ny < N:
                # Calculate the height difference between the current cell and the neighbor
                height_diff = abs(grid[nx][ny] - grid[x][y])
                
                # The required ladder length is the maximum of the height difference and the current distance
                new_ladder_length = max(d, height_diff)
                
                # If this new ladder length is shorter than the previously recorded distance, update it
                if new_ladder_length < dist[nx][ny]:
                    dist[nx][ny] = new_ladder_length
                    heapq.heappush(pq, (new_ladder_length, nx, ny))
    
    # If we reach here, it means the path is not possible (which shouldn't happen with valid input)
    return -1

# Read input
M, N = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(M)]

# Output the result
print(min_ladder_length(grid))