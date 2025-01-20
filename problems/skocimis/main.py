def max_moves(A, B, C):
    moves = 0
    while True:
        if abs(A - B) > abs(B - C):
            A, B = B + (B - C), B
        elif abs(A - B) < abs(B - C):
            B, C = A + (C - A), C
        else:
            break
        moves += 1
    return moves

# Sample Input 1
A, B, C = 2, 3, 5
print(max_moves(A, B, C))  # Output: 1

# Sample Input 2
A, B, C = 3, 5, 9
print(max_moves(A, B, C))  # Output: 3