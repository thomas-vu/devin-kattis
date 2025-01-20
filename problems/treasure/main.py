from collections import deque

def min_days_to_treasure(N, M, K, grid):
    start = (-1, -1)
    end = (-1, -1)
    
    # Find the start and end positions
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 'S':
                start = (i, j)
            elif grid[i][j] == 'G':
                end = (i, j)
    
    # BFS initialization
    visited = [[False] * M for _ in range(N)]
    stamina_cost = [[float('inf')] * M for _ in range(N)]
    queue = deque([(start[0], start[1], K, 0)])  # (row, col, remaining stamina, days)
    stamina_cost[start[0]][start[1]] = K
    
    # Directions for moving up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while queue:
        x, y, stamina, days = queue.popleft()
        
        # If out of bounds or in river or already visited with less stamina
        if x < 0 or x >= N or y < 0 or y >= M or grid[x][y] == '#' or visited[x][y]:
            continue
        
        # Update the stamina cost for this cell
        if grid[x][y] == '.':
            cost = 1
        elif grid[x][y] == 'F':
            cost = 2
        elif grid[x][y] == 'M':
            cost = 3
        
        if stamina - cost < 0:
            # Cannot move further, rest for the next day
            if stamina_cost[x][y] < float('inf'):
                continue  # Already visited with less stamina
            stamina_cost[x][y] = stamina
            queue.append((x, y, K, days + 1))
        else:
            # Move to the next cell with updated stamina and days
            if (x, y) == end:
                return days + 1
            stamina_cost[x][y] = stamina - cost
            visited[x][y] = True
            for dx, dy in directions:
                queue.append((x + dx, y + dy, stamina - cost, days + 1))
    
    return -1

# Read input
N, M, K = map(int, input().split())
grid = [input() for _ in range(N)]

# Output the result
print(min_days_to_treasure(N, M, K, grid))