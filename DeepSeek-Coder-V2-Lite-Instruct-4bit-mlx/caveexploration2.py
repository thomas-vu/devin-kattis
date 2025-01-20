from heapq import heappop, heappush

def min_hours(N, heights):
    # Directions for moving up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # Priority queue to store the minimum hours needed to reach each position
    pq = [(0, 0, 0)]  # (hours, x, y)
    visited = [[False] * N for _ in range(N)]
    
    while pq:
        hours, x, y = heappop(pq)
        
        # If reached the exit
        if x == N - 1 and y == N - 1:
            return hours
        
        # If already visited this position with less or equal hours
        if visited[x][y] and visited[x][y] <= hours:
            continue
        
        visited[x][y] = True
        
        # Explore all possible directions
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                # Calculate the required hours to swim to the next position
                next_hours = max(hours, heights[nx][ny])
                heappush(pq, (next_hours, nx, ny))
    
    return -1  # This should never be reached if the input is valid

# Read input
N = int(input())
heights = [list(map(int, input().split())) for _ in range(N)]

# Calculate and output the minimum number of hours
print(min_hours(N, heights))