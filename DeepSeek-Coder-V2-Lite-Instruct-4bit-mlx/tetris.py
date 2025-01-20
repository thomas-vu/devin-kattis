def count_configurations(C, P, heights):
    # Define the tetromino shapes and rotations
    tetrominos = [
        [],  # Placeholder for index 0
        [[0], [0], [0], [0]],  # I-shape (1)
        [[0, 0]],  # O-shape (2)
        [[1, 0], [1, 1], [0, 1], [1, -1]],  # T-shape (3)
        [[0, 0], [0, -1], [0, 1], [0, 2]],  # S-shape (4)
        [[0, 0], [1, 0], [-1, 0], [0, -1]],  # Z-shape (5)
        [[0, 0], [0, -1], [0, 1], [1, 1]],  # L-shape (6)
        [[0, 0], [0, -1], [0, 1], [-1, 1]]  # J-shape (7)
    ]
    
    def can_fit(x, y, piece):
        for dx, dy in piece:
            nx, ny = x + dx, y + dy
            if 0 <= nx < C and heights[nx] > ny:
                return False
        return True
    
    def place(x, y, piece):
        for dx, dy in piece:
            nx, ny = x + dx, y + dy
            heights[nx] = min(heights[nx], ny)
    
    def remove(x, y, piece):
        for dx, dy in piece:
            nx, ny = x + dx, y + dy
            heights[nx] = max(heights[nx], ny)
    
    def dfs(index, x, y):
        if index == len(tetrominos[P]):
            return 1
        
        piece = tetrominos[P][index]
        count = 0
        for nx in range(C):
            if can_fit(nx, heights[nx], piece):
                place(nx, heights[nx], piece)
                count += dfs(index + 1, nx, heights[nx] + 1)
                remove(nx, heights[nx], piece)
        return count
    
    return dfs(0, 0, 0)

# Read input
C, P = map(int, input().split())
heights = list(map(int, input().split()))

# Calculate and output the result
print(count_configurations(C, P, heights))