def can_rook_reach_target(r, c, board):
    # Find the position of the rook and the target square
    for i in range(r):
        for j in range(c):
            if board[i][j] == 'R':
                rook_pos = (i, j)
            elif board[i][j] == 'T':
                target_pos = (i, j)
    
    # Check if the rook can move to the target square without capturing any knight
    def is_safe(x, y):
        for i in range(r):
            for j in range(c):
                if board[i][j] == 'K':
                    for dx, dy in [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]:
                        if x + dx == i and y + dy == j:
                            return False
        return True
    
    # Check if the target square is safe without capturing any knight
    if not is_safe(target_pos[0], target_pos[1]):
        return "no"
    
    # Check if the rook can move to the target square without capturing any knight
    def bfs():
        visited = [[False] * c for _ in range(r)]
        queue = [(rook_pos[0], rook_pos[1], 0)]
        visited[rook_pos[0]][rook_pos[1]] = True
        while queue:
            x, y, dist = queue.pop(0)
            if (x, y) == target_pos:
                return True
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny] and is_safe(nx, ny):
                    visited[nx][ny] = True
                    queue.append((nx, ny, dist + 1))
        return False
    
    if bfs():
        return "yes"
    else:
        return "no"

# Read input
r, c = map(int, input().split())
board = [input() for _ in range(r)]

# Output the result
print(can_rook_reach_target(r, c, board))