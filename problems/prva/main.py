def find_smallest_word(R, C, grid):
    words = []
    
    # Check horizontally (left to right)
    for i in range(R):
        word = ''
        for j in range(C):
            if grid[i][j] != '#':
                word += grid[i][j]
            else:
                if len(word) >= 2:
                    words.append(word)
                word = ''
        if len(word) >= 2:
            words.append(word)
    
    # Check vertically (top to bottom)
    for j in range(C):
        word = ''
        for i in range(R):
            if grid[i][j] != '#':
                word += grid[i][j]
            else:
                if len(word) >= 2:
                    words.append(word)
                word = ''
        if len(word) >= 2:
            words.append(word)
    
    # Find the lexicographically smallest word
    min_word = min(words)
    return min_word

# Read input
R, C = map(int, input().split())
grid = [input() for _ in range(R)]

# Find and print the result
result = find_smallest_word(R, C, grid)
print(result)