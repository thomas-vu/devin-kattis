def min_distance(n, k, tiles):
    from collections import deque
    
    # Find the positions of all numbers 1 to k
    positions = {}
    for i in range(n):
        for j in range(n):
            num = tiles[i][j]
            if num not in positions:
                positions[num] = []
            positions[num].append((i, j))
    
    # BFS to find the shortest path from any 1 tile to any k tile
    queue = deque()
    visited = set()
    
    # Start from all tiles numbered 1
    for start in positions[1]:
        queue.append((start, 0))
        visited.add(start)
    
    while queue:
        (x, y), dist = queue.popleft()
        
        # If we reach a tile numbered k, return the distance
        if tiles[x][y] == k:
            return dist
        
        # Explore all 4 possible directions (up, down, left, right)
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited:
                queue.append(((nx, ny), dist + 1))
                visited.add((nx, ny))
    
    # If no path is found, return -1
    return -1

# Read input
n, k = map(int, input().split())
tiles = [list(map(int, input().split())) for _ in range(n)]

# Output the result
print(min_distance(n, k, tiles))