from collections import deque

def min_hops(R, C, GR, GC, LR, LC):
    if (GR, GC) == (LR, LC):
        return 0
    
    # Directions a knight can move: (±2, ±1) or (±1, ±2)
    directions = [(2, 1), (1, 2), (-1, -2), (-2, -1), (-2, 1), (1, -2), (-1, 2), (2, -1)]
    
    # BFS setup
    queue = deque([(GR, GC, 0)])  # (row, col, hops)
    visited = set((GR, GC))
    
    while queue:
        r, c, hops = queue.popleft()
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            
            if 1 <= nr <= R and 1 <= nc <= C and (nr, nc) not in visited:
                if (nr, nc) == (LR, LC):
                    return hops + 1
                queue.append((nr, nc, hops + 1))
                visited.add((nr, nc))
    
    return "impossible"

# Read input and process each test case
while True:
    try:
        R, C, GR, GC, LR, LC = map(int, input().split())
        print(min_hops(R, C, GR, GC, LR, LC))
    except EOFError:
        break