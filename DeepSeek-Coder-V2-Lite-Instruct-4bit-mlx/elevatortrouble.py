from collections import deque

def min_button_presses(f, s, g, u, d):
    visited = [False] * (f + 1)
    queue = deque([(s, 0)])  # (current floor, number of presses)
    visited[s] = True
    
    while queue:
        current_floor, num_presses = queue.popleft()
        
        if current_floor == g:
            return num_presses
        
        up_floor = current_floor + u
        down_floor = current_floor - d
        
        if up_floor <= f and not visited[up_floor]:
            queue.append((up_floor, num_presses + 1))
            visited[up_floor] = True
        
        if down_floor > 0 and not visited[down_floor]:
            queue.append((down_floor, num_presses + 1))
            visited[down_floor] = True
    
    return "use the stairs"

# Read input
f, s, g, u, d = map(int, input().split())
result = min_button_presses(f, s, g, u, d)
print(result)