def min_strokes(r, c, keyboard, text):
    # Define the four possible movements for the cursor
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    # Function to perform a breadth-first search (BFS) from each key
    def bfs(start):
        queue = [start]
        visited[start[0]][start[1]] = True
        min_strokes = 0
        
        while queue:
            x, y = queue.pop(0)
            min_strokes += 1
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
        
        return min_strokes
    
    # Initialize the visited matrix and calculate strokes for each key
    visited = [[False] * c for _ in range(r)]
    total_strokes = 0
    
    for char in text:
        found = False
        for i in range(r):
            for j in range(c):
                if keyboard[i][j] == char:
                    total_strokes += bfs((i, j)) - 1  # Subtract 1 for the initial position
                    found = True
                    break
            if found:
                break
    
    return total_strokes + 1  # Add 1 for the Enter key at the end

# Read input
r, c = map(int, input().split())
keyboard = [input() for _ in range(r)]
text = input()

# Output the result
print(min_strokes(r, c, keyboard, text))