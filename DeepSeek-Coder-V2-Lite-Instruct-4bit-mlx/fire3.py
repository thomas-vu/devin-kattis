from collections import deque

def bfs(maze, R, C):
    fire_queue = deque()
    joe_queue = deque()
    
    # Initialize fire and Joe positions
    for r in range(R):
        for c in range(C):
            if maze[r][c] == 'F':
                fire_queue.append((r, c))
            elif maze[r][c] == 'J':
                joe_queue.append((r, c))
    
    # Directions Joe can move: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # BFS for fire spread and Joe movement
    time = 0
    while joe_queue:
        # Fire spread
        fire_size = len(fire_queue)
        for _ in range(fire_size):
            fr, fc = fire_queue.popleft()
            for dr, dc in directions:
                nr, nc = fr + dr, fc + dc
                if 0 <= nr < R and 0 <= nc < C and maze[nr][nc] == '.':
                    maze[nr][nc] = 'F'
                    fire_queue.append((nr, nc))
        
        # Joe movement
        joe_size = len(joe_queue)
        for _ in range(joe_size):
            jr, jc = joe_queue.popleft()
            if (jr == 0 or jr == R - 1 or jc == 0 or jc == C - 1):
                return time + 1
            for dr, dc in directions:
                nr, nc = jr + dr, jc + dc
                if 0 <= nr < R and 0 <= nc < C and maze[nr][nc] == '.':
                    maze[nr][nc] = 'J'
                    joe_queue.append((nr, nc))
        
        time += 1
    
    return "IMPOSSIBLE"

# Read input
R, C = map(int, input().split())
maze = [list(input()) for _ in range(R)]

# Output the result of Joe's escape plan
print(bfs(maze, R, C))