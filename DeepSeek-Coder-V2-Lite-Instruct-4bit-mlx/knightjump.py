from collections import deque

def min_knight_moves(N, board):
    # Directions a knight can move
    directions = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
    
    # Find the starting position of the knight
    start = None
    for i in range(N):
        for j in range(N):
            if board[i][j] == 'K':
                start = (i + 1, j + 1)
                break
        if start:
            break
    
    # If the starting position is (1, 1), return -1 as it's not reachable
    if start == (1, 1):
        return -1
    
    # BFS initialization
    queue = deque([(start[0], start[1], 0)])  # (row, col, distance)
    visited = set([start])
    
    while queue:
        r, c, dist = queue.popleft()
        
        # Check if the knight has reached (1, 1)
        if (r, c) == (1, 1):
            return dist
        
        # Explore all possible moves
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 1 <= nr <= N and 1 <= nc <= N and (nr, nc) not in visited:
                if board[nr - 1][nc - 1] == '.':
                    visited.add((nr, nc))
                    queue.append((nr, nc, dist + 1))
    
    return -1

# Read input
N = int(input())
board = [input() for _ in range(N)]

# Output the result
print(min_knight_moves(N, board))