def max_resources(n, f, matrix):
    from collections import deque
    
    # Directions for moving up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # Initialize the best path and a queue for BFS
    best = 0
    queue = deque()
    
    # Start BFS from each cell on the border
    for i in range(n):
        for j in range(n):
            if (i == 0 or i == n - 1 or j == 0 or j == n - 1):
                queue.append((i, j, matrix[i][j]))
    
    # BFS to find the maximum resources path
    while queue:
        x, y, current_resources = queue.popleft()
        
        # If the fuel is 0, stop this path
        if f == 0:
            continue
        
        # Update the best path with the current resources
        best = max(best, current_resources)
        
        # Explore adjacent planets within fuel range
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < n and 0 <= ny < n:
                next_resources = current_resources + matrix[nx][ny]
                
                # If the next planet has more resources and can be reached with fuel
                if matrix[nx][ny] > current_resources:
                    queue.append((nx, ny, next_resources))
    
    return best

# Read input
n, f = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

# Calculate and print the result
print(max_resources(n, f, matrix))