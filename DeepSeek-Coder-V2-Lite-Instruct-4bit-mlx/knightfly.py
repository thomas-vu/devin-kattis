def min_knight_flies(N, start, end, clear_cells):
    from collections import deque
    
    # Convert clear cells to a set for fast lookup
    clear_set = {(x, y) for x, y in clear_cells}
    
    # Directions a knight can move
    directions = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]
    
    # BFS to find the minimum number of knight flies
    queue = deque([(start[0], start[1], 0)])  # (x, y, distance)
    visited = set([(start[0], start[1])])
    
    while queue:
        x, y, dist = queue.popleft()
        
        if (x, y) == end:
            return dist
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            while (nx, ny) in clear_set:
                if not visited.get((nx, ny)):
                    queue.append((nx, ny, dist + 1))
                    visited.add((nx, ny))
                nx += dx
                ny += dy
    
    return -1

# Read input
N = int(input())
Xs, Ys, Xt, Yt = map(int, input().split())
clear_cells = [tuple(map(int, input().split())) for _ in range(N)]

# Solve the problem and output the result
print(min_knight_flies(N, (Xs, Ys), (Xt, Yt), clear_cells))