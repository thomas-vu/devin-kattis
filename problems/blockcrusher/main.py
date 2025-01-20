def find_fracture_line(block):
    h, w = len(block), len(block[0])
    min_strength = float('inf')
    best_path = None
    
    # Directions for moving in the grid: right, down, left, up, and diagonals
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    
    # Helper function to perform DFS and find the minimum strength path
    def dfs(x, y, visited, current_strength):
        nonlocal min_strength, best_path
        
        # If we've reached the bottom edge, check if this is the best path so far
        if x == h - 1:
            if current_strength < min_strength:
                min_strength = current_strength
                best_path = visited.copy()
            return
        
        # Explore all possible directions
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < h and 0 <= ny < w and (nx, ny) not in visited:
                visited.add((nx, ny))
                dfs(nx, ny, visited, current_strength + int(block[nx][ny]))
                visited.remove((nx, ny))
    
    # Start DFS from each square on the top edge
    for start_x in range(h):
        for start_y in range(w):
            dfs(start_x, start_y, {(start_x, start_y)}, int(block[start_x][start_y]))
    
    # Mark the fracture line with spaces
    for x, y in best_path:
        block[x] = block[x][:y] + ' ' + block[x][y+1:]
    
    return block

def main():
    while True:
        h, w = map(int, input().split())
        if h == 0 and w == 0:
            break
        block = [input().strip() for _ in range(h)]
        result = find_fracture_line(block)
        for line in result:
            print(line)
        print()

if __name__ == "__main__":
    main()