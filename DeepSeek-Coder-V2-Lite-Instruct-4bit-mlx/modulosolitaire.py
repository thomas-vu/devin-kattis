from collections import deque

def min_moves(m, n, s0, operations):
    visited = set()
    queue = deque([(s0, 0)])
    
    while queue:
        current, moves = queue.popleft()
        
        if current == 0:
            return moves
        
        for ai, bi in operations:
            next_val = (current * ai + bi) % m
            if next_val not in visited:
                visited.add(next_val)
                queue.append((next_val, moves + 1))
    
    return -1

# Read input
m, n, s0 = map(int, input().split())
operations = [tuple(map(int, input().split())) for _ in range(n)]

# Calculate and print the result
print(min_moves(m, n, s0, operations))