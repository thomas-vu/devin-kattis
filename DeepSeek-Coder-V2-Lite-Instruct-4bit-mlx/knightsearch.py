def can_find_icpcasia(N, S):
    # Define the knight's possible moves in (row, column) format
    knight_moves = [(2, 1), (2, -1), (-2, 1), (-2, -1),
                    (1, 2), (1, -2), (-1, 2), (-1, -2)]
    
    # Convert the string representation of the board into a 2D list for easy access
    board = [list(S[i*N:(i+1)*N]) for i in range(N)]
    
    # Find the initial position of 'I'
    for r in range(N):
        for c in range(N):
            if board[r][c] == 'I':
                # Use DFS to search for the rest of the string
                if dfs(board, r, c, "ICPCASIASG", N):
                    return "YES"
    return "NO"

def dfs(board, row, col, target, N):
    # Base case: if the target string is empty, return True
    if not target:
        return True
    
    # Mark the current cell as visited by setting it to '#'
    temp, board[row][col] = board[row][col], '#'
    
    # Explore all possible knight moves from the current cell
    for move in knight_moves:
        new_row, new_col = row + move[0], col + move[1]
        if 0 <= new_row < N and 0 <= new_col < N and board[new_row][new_col] == target[0]:
            if dfs(board, new_row, new_col, target[1:], N):
                return True
    
    # Restore the cell's original value (backtrack)
    board[row][col] = temp
    
    return False

# Read input
N = int(input())
S = input()

# Output the result
print(can_find_icpcasia(N, S))