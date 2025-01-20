def find_shortest_path(r, d):
    # Directions for moving right and up in the grid
    directions = [(0, 1), (1, 0)]
    
    # Initialize the queue for BFS with the starting position and path
    queue = [(0, 0, [str(0) + ' ' + str(0)])]
    visited = set()
    
    while queue:
        x, y, path = queue.pop(0)
        
        # If the robot has vacuumed the entire room, return the path
        if x == r - 1 and y == d - 1:
            return path
        
        # Mark the current position as visited
        visited.add((x, y))
        
        # Explore all possible moves from the current position
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            # Check if the new position is within bounds and not visited
            if 0 <= nx < r and 0 <= ny < d and (nx, ny) not in visited:
                # Update the path with the new position
                new_path = path + ' ' + str(nx) + ' ' + str(ny)
                # Add the new position to the queue
                queue.append((nx, ny, new_path))
    
    return "No path found"

# Read input from standard input
r, d = map(int, input().split())
print(find_shortest_path(r, d))