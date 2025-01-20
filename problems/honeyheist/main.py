def bfs(start, goal, honeycomb, hardened):
    queue = [(start, 0)]
    visited = set([start])
    
    while queue:
        current, depth = queue.pop(0)
        
        if current == goal:
            return depth
        
        for neighbor in honeycomb[current]:
            if neighbor not in visited and neighbor not in hardened:
                visited.add(neighbor)
                queue.append((neighbor, depth + 1))
    
    return float('inf')

R, N, A, B, X = map(int, input().split())
hardened_cells = set(map(int, input().split()))

honeycomb = {}
for i in range(1, R**3 - (R-1)**3 + 1):
    honeycomb[i] = []

# Define the hexagonal grid structure
for i in range(1, R**3 - (R-1)**3 + 1):
    neighbors = []
    # Determine the position of the cell in the hexagonal grid
    row, col = (i - 1) // R + 1, (i - 1) % R
    # Define the six possible directions in a hexagonal grid
    hex_directions = [(-1, 0), (-1, 1), (0, 1), (1, 0), (1, -1), (0, -1)]
    
    for dr, dc in hex_directions:
        new_row, new_col = row + dr, col + dc
        if 1 <= new_row <= R and 1 <= new_col <= (R - abs(new_row - (R-1)/2)) * 2:
            new_cell = new_row * R + new_col
            if new_cell != i and new_cell <= R**3 - (R-1)**3:
                neighbors.append(new_cell)
    
    honeycomb[i] = neighbors

distance = bfs(A, B, honeycomb, hardened_cells)
if distance <= N:
    print(distance)
else:
    print("No")