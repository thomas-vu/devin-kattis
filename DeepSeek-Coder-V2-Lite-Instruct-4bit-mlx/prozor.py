def find_max_flies(R, S, K, picture):
    max_flies = 0
    best_x, best_y = -1, -1
    
    for x in range(R):
        for y in range(S):
            if picture[x][y] == '*':
                # Check for the top and bottom of the racket
                if x + K <= R:
                    flies = 0
                    for i in range(x, x + K):
                        for j in range(y - (K // 2), y + (K // 2) + 1):
                            if j >= 0 and j < S:
                                if picture[i][j] == '*':
                                    flies += 1
                    if flies > max_flies:
                        max_flies = flies
                        best_x, best_y = x, y
                # Check for the left and right of the racket
                if y + K <= S:
                    flies = 0
                    for j in range(y, y + K):
                        for i in range(x - (K // 2), x + (K // 2) + 1):
                            if i >= 0 and i < R:
                                if picture[i][j] == '*':
                                    flies += 1
                    if flies > max_flies:
                        max_flies = flies
                        best_x, best_y = x, y
    
    # Mark the best position with the racket
    result_picture = [list(row) for row in picture]
    for i in range(best_x - (K // 2), best_x + (K // 2) + 1):
        for j in range(best_y - (K // 2), best_y + (K // 2) + 1):
            if i >= 0 and i < R and j >= 0 and j < S:
                result_picture[i][j] = '+' if (i == best_x - (K // 2) or i == best_x + (K // 2)) and (j == best_y - (K // 2) or j == best_y + (K // 2)) else '-' if i != best_x and j == best_y else '|'
    
    return max_flies, result_picture

# Read input
R, S, K = map(int, input().split())
picture = [input() for _ in range(R)]

# Process and output the result
max_flies, result_picture = find_max_flies(R, S, K, picture)
print(max_flies)
for row in result_picture:
    print(''.join(row))