def find_shortest_path(board):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
    dir_dict = {'>': 0, 'v': 1, '<': 2, '^': 3}
    dir_chars = ['>', 'v', '<', '^']
    
    def is_valid(x, y):
        return 0 <= x < 8 and 0 <= y < 8 and board[x][y] != 'C'
    
    def bfs():
        queue = [(0, 0, dir_dict['>'], [])]  # (x, y, direction, path)
        visited = set((0, 0, dir_dict['>']))
        
        while queue:
            x, y, direction, path = queue.pop(0)
            
            if (x, y) == goal:
                return path + ['T']
            
            # Move forward
            dx, dy = directions[direction]
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny) and (nx, ny, direction) not in visited:
                queue.append((nx, ny, direction, path + ['F']))
                visited.add((nx, ny, direction))
            
            # Turn right
            new_direction = (direction + 1) % 4
            if (x, y, new_direction) not in visited:
                queue.append((x, y, new_direction, path + ['R']))
                visited.add((x, y, new_direction))
            
            # Turn left
            new_direction = (direction - 1) % 4
            if (x, y, new_direction) not in visited:
                queue.append((x, y, new_direction, path + ['L']))
                visited.add((x, y, new_direction))
            
            # Fire laser
            if board[x][y] == 'I':
                board[x][y] = '.'
            elif not is_valid(x, y):
                continue
            
            for _ in range(3):  # Fire laser multiple times if needed
                dx, dy = directions[direction]
                nx, ny = x + dx, y + dy
                if not is_valid(nx, ny):
                    break
                if board[nx][ny] == 'I':
                    board[nx][ny] = '.'
                x, y = nx, ny
            
            if (x, y, direction) not in visited:
                queue.append((x, y, direction, path + ['X']))
                visited.add((x, y, direction))
        
        return "no solution"
    
    goal = None
    for i in range(8):
        for j in range(8):
            if board[i][j] == 'D':
                goal = (i, j)
                break
        if goal:
            break
    
    return bfs()

# Read input
board = [list(input().strip()) for _ in range(8)]
# Output the result
print('\n'.join(''.join(row) for row in find_shortest_path(board)))