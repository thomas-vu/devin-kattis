def find_longest_loop(s, c):
    # Define the turns and their corresponding characters
    turn_map = {
        'L': {'L': -1, 'R': 1},
        'R': {'L': 1, 'R': -1}
    }
    
    # Define the directions and their corresponding movements
    directions = {
        0: (0, 1),  # right
        1: (1, 0),  # down
        2: (0, -1), # left
        3: (-1, 0)  # up
    }
    
    def simulate(s, c, start_dir):
        x, y = 0, 0
        dir_idx = start_dir
        visited = set()
        path = []
        
        while True:
            # Mark the current position as visited
            pos = (x, y)
            if pos in visited:
                break
            visited.add(pos)
            
            # Append the current segment to the path
            if dir_idx == 0:
                path.append('R')
            elif dir_idx == 1:
                path.append('L')
            elif dir_idx == 2:
                path.append('S')
            else:
                path.append('R' if turn_map['L']['R'] == 1 else 'L')
            
            # Move to the next position based on the current direction
            dx, dy = directions[dir_idx]
            nx, ny = x + dx, y + dy
            
            # Check if the next position is valid (within bounds and not visited)
            if nx < 0 or nx >= s + c or ny < 0 or ny >= max(s, c):
                break
            
            # Update the position and direction based on the track segment
            if (nx, ny) in visited:
                break
            x, y = nx, ny
            
            # Update the direction based on the next turn
            if (nx, ny) in visited:
                break
            
            # Check the next track segment and update the direction accordingly
            if (x, y) in visited:
                break
            
            next_track = grid[x][y]
            if next_track in turn_map:
                dir_idx = (dir_idx + turn_map[next_track]['R']) % 4
            
            # If no more segments can be added, break the loop
            if len(path) >= s + c:
                break
        
        return path
    
    # Simulate the tracks and find the longest loop
    max_loop = []
    for start_dir in range(4):
        loop = simulate(s, c, start_dir)
        if len(loop) > len(max_loop):
            max_loop = loop
    
    return ''.join(max_loop)

# Read input from stdin
s, c = map(int, input().split())
print(find_longest_loop(s, c))